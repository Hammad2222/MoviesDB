-- 03_load_ratings.sql
COPY ratings (
  userId,
  movieId,
  rating,
  timestamp
)
FROM '/data/ratings.csv'
WITH (
  FORMAT csv,
  HEADER true
);

