import json
import os
from typing import List, Optional, AsyncIterator

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import redis.asyncio as redis

from database import SessionLocal
from models import MovieMetadata
from schemas import MovieMetadataSchema

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CACHE_TTL = int(os.getenv("CACHE_TTL", 3600))  # 1‑hour default

redis_client: Optional[redis.Redis] = None  # will be initialised in lifespan

# --- Lifespan -------------------------------------------------------------
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """FastAPI 0.111+ preferred way to manage startup/shutdown resources."""
    global redis_client
    redis_client = redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
    yield  # ⟵ application runs here
    if redis_client is not None:
        await redis_client.close()

app = FastAPI(title="Movie Search API", lifespan=lifespan)

# --- Database dependency ---------------------------------------------------
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Redis helpers ---------------------------------------------------------
async def cache_get(key: str):
    if redis_client is None:
        return None
    return await redis_client.get(key)

async def cache_set(key: str, value: dict):
    if redis_client is None:
        return
    # default=str converts date → "1995-10-30"
    await redis_client.set(key, json.dumps(value, default=str), ex=CACHE_TTL)


# --- Endpoints -------------------------------------------------------------
@app.get("/movies/{movie_id}", response_model=MovieMetadataSchema)
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    cache_key = f"movie:{movie_id}"
    if cached := await cache_get(cache_key):
        return json.loads(cached)

    movie = db.query(MovieMetadata).filter(MovieMetadata.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    data = MovieMetadataSchema.from_orm(movie).model_dump()
    await cache_set(cache_key, data)
    return data

@app.get("/search/", response_model=List[MovieMetadataSchema])
async def search_movies(q: str, limit: int = 10, db: Session = Depends(get_db)):
    cache_key = f"search:{q.lower()}:{limit}"
    if cached := await cache_get(cache_key):
        return json.loads(cached)

    results = (
        db.query(MovieMetadata)
        .filter(MovieMetadata.original_title.ilike(f"%{q}%"))
        .limit(limit)
        .all()
    )
    if not results:
        raise HTTPException(status_code=404, detail="No movies match your query")

    data = [MovieMetadataSchema.from_orm(m).model_dump() for m in results]
    await cache_set(cache_key, data)
    return data