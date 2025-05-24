-- 02_load_movies_metadata.sql

COPY movies_metadata (
  adult,
  belongs_to_collection,
  budget,
  genres,
  homepage,
  id,
  imdb_id,
  original_language,
  original_title,
  overview,
  popularity,
  poster_path,
  production_companies,
  production_countries,
  release_date,
  revenue,
  runtime,
  spoken_languages,
  status,
  tagline,
  title,
  video,
  vote_average,
  vote_count
)
FROM '/data/movies_metadata.csv'
WITH (
  FORMAT csv,
  HEADER true,
  DELIMITER ',',
  QUOTE '"'
);
