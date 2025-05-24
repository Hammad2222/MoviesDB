# Movie Search Application

A lightweight FastAPI service that lets you search **The Movies Dataset** from Kaggle and fetch detailed metadata for any film.  
Behind the scenes it uses PostgreSQL for persistence, Redis for caching, and is fronted by Nginx as a reverse‑proxy.


---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 Search | `GET /search/?q=<title>&limit=10` – fuzzy search by original title |
| 🎞️ Details | `GET /movies/{id}` – returns full metadata for a single movie |
| ⚡ Caching | Hot queries are served from Redis with a configurable TTL (default 1 hour) |
| 🐳 One‑command setup | `docker compose up -d` spins up Postgres, Redis, FastAPI & Nginx |
| 📚 Auto‑docs | Swagger UI available at `/docs`, ReDoc at `/redoc` |

---

## 🚀 Quick Start

> **Pre‑requisite:** [Docker Desktop](https://docs.docker.com/get-docker/) or Docker Engine + Compose plugin.

```bash
# clone the repo
$ git clone https://github.com/your‑org/fastapi‑movie‑app.git
$ cd fastapi-movie-app

# launch the entire stack
$ docker compose up -d --build

# open the docs
👉  http://localhost/docs
```

### Example calls

```bash
# Search the catalogue
curl "http://localhost/search/?q=Toy%20Story&limit=5"

# Fetch movie by TMDB id
curl http://localhost/movies/862
```

---

## 🗄️ Stack

| Layer | Tech | Why |
|-------|------|-----|
| API   | **FastAPI + Uvicorn** | Modern, async, auto‑docs |
| Cache | **Redis 8** | Ultra‑fast in‑memory caching |
| DB    | **PostgreSQL 16** | Robust relational store |
| Proxy | **Nginx 1.27** | TLS termination & routing |
| Orchestration | **Docker Compose v3.8** | One‑command dev environment |

Two Docker networks are defined:

* **`front_net`** – public edge (`nginx` ⇄ `web`)
* **`back_net`** – internal services (`web` ⇄ `db` & `redis`)

---

## 📂 Dataset

This project ships with the public **[The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)** (24 MB compressed).  
During the first run, the CSVs are imported into Postgres via `COPY` commands found in `db/init/`.

---

## 🛠️ Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `DATABASE_URL` | `postgresql://postgres:postgres@db:5432/movies` | SQLAlchemy connection string |
| `REDIS_URL`    | `redis://redis:6379/0` | Redis connection string |
| `CACHE_TTL`    | `3600` | Cache entry lifetime (seconds) |

Override them in `.env` or directly in `docker-compose.yml`.

---

## 🏗️ Project Structure

> *Only key paths shown – see full tree in repo.*

```
fastapi_movie_app/
├── app/                # FastAPI application package
│   ├── main.py         # entry point with routes
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic response models
│   └── database.py     # engine & session helper
├── db/init/            # SQL bootstrap & COPY scripts
├── nginx/              # Dockerfile + movies.conf
├── docker-compose.yml
└── README.md           # you’re here ✅
```

---

## 🔒 Security Notes

* Minimal **Alpine/Slim images** reduce surface area.
* Separate front/back networks prevent direct DB/Redis exposure.
* Nginx can be extended with Let’s Encrypt TLS (see `docs/ssl.md`).

---

## 📜 License

Released under the MIT License – see `LICENSE` for details.

---

## 👥 Contributing

1. Fork the repo & create a new branch.
2. Commit your changes with clear messages.
3. Open a Pull Request – we’ll review ASAP!

Thanks for checking out the Movie Search App 🎬🍿

---
