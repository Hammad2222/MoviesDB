from pydantic import BaseModel
from typing import Optional
from datetime import date

class MovieMetadataSchema(BaseModel):
    id: int
    adult: Optional[bool]
    original_title: Optional[str]
    overview: Optional[str]
    release_date: Optional[date]   # accept dates directly
    popularity: Optional[float]
    vote_average: Optional[float]
    vote_count: Optional[float]

    class Config:
        from_attributes = True  # Pydantic v2 replacement for orm_mode