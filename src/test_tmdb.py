import os

from dotenv import load_dotenv

from tmdb_client import TMDBClient


load_dotenv()

token = os.getenv("TMDB_TOKEN")

if not token:
    raise RuntimeError(
        "TMDB_TOKEN no está definido"
    )


client = TMDBClient(token)

movie = client.get_movie(496243)


print("=== MOVIE ===")

print("TMDB ID:", movie["id"])
print("Title:", movie["title"])
print("Original title:", movie["original_title"])
print("Original language:", movie["original_language"])

print()
print("=== RELEASE ===")

print("Release date:", movie["release_date"])
print("Runtime:", movie["runtime"])
print("Status:", movie["status"])

print()
print("=== RATINGS ===")

print("TMDB rating:", movie["vote_average"])
print("TMDB votes:", movie["vote_count"])
print("Popularity:", movie["popularity"])

print()
print("=== MONEY ===")

print("Budget:", movie["budget"])
print("Revenue:", movie["revenue"])

print()
print("=== GENRES ===")

for genre in movie["genres"]:
    print(
        f"{genre['id']} - {genre['name']}"
    )

print()
print("=== PRODUCTION COMPANIES ===")

for company in movie["production_companies"]:
    print(
        f"{company['id']} - {company['name']}"
    )

print()
print("=== PRODUCTION COUNTRIES ===")

for country in movie["production_countries"]:
    print(
        f"{country['iso_3166_1']} - {country['name']}"
    )

print()
print("=== SPOKEN LANGUAGES ===")

for language in movie["spoken_languages"]:
    print(
        f"{language['iso_639_1']} - {language['name']}"
    )

print()
print("=== CREDITS ===")

print(
    "Cast:",
    len(movie["credits"]["cast"])
)

print(
    "Crew:",
    len(movie["credits"]["crew"])
)

print()
print("=== KEYWORDS ===")

for keyword in movie["keywords"]["keywords"]:
    print(
        f"{keyword['id']} - {keyword['name']}"
    )

print()
print("=== EXTERNAL IDS ===")

print(movie["external_ids"])

print()
print("=== VIDEOS ===")

print(
    "Videos:",
    len(movie["videos"]["results"])
)

print()
print("=== RELEASE DATES ===")

print(
    "Countries:",
    len(movie["release_dates"]["results"])
)