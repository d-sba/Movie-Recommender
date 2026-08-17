CREATE OR REPLACE TABLE stg_letterboxd AS
SELECT
    CAST(Date AS DATE) AS watched_date,
    TRIM(Name) AS name,
    CAST(Year AS INTEGER) AS year,

    "Letterboxd URI" AS letterboxd_uri,

    regexp_extract(
        "Letterboxd URI",
        'boxd\.it/([^/?]+)',
        1
    ) AS letterboxd_id,

    CAST(Rating AS DOUBLE) AS rating

FROM read_csv(
    'data/raw/letterboxd/ratings.csv',
    header = true
);