CREATE OR REPLACE TABLE stg_tmdb_movies AS

SELECT
    *
FROM read_json_auto(
    'data/raw/tmdb/movies/*.json'
);