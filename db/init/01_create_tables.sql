-- 01_create_tables.sql

-- movies_metadata
CREATE TABLE IF NOT EXISTS movies_metadata (
  id                   BIGINT,
  adult                BOOLEAN,
  belongs_to_collection JSONB,
  budget               BIGINT,
  genres               JSONB,
  homepage             TEXT,
  imdb_id              TEXT,
  original_language    TEXT,
  original_title       TEXT,
  overview             TEXT,
  popularity           DOUBLE PRECISION,
  poster_path          TEXT,
  production_companies JSONB,
  production_countries JSONB,
  release_date         DATE,
  revenue              BIGINT,
  runtime              DOUBLE PRECISION,
  spoken_languages     JSONB,
  status               TEXT,
  tagline              TEXT,
  title                TEXT,
  video                BOOLEAN,
  vote_average         DOUBLE PRECISION,
  vote_count           INTEGER
);

-- ratings
CREATE TABLE IF NOT EXISTS ratings (
  userId    INTEGER,
  movieId   BIGINT,
  rating    NUMERIC(3,1),
  timestamp BIGINT
);

