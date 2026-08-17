import json
import os
from pathlib import Path

import duckdb
from dotenv import load_dotenv

from tmdb_client import TMDBClient


ROOT = Path(__file__).resolve().parents[1]

DB_PATH = ROOT / "db" / "movies.duckdb"
RAW_PATH = ROOT / "data" / "raw" / "tmdb" / "movies"


def save_raw_movie(tmdb_id: int, data: dict) -> Path:

    RAW_PATH.mkdir(
        parents=True,
        exist_ok=True,
    )

    path = RAW_PATH / f"{tmdb_id}.json"

    with path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )

    return path


def main():

    load_dotenv()

    token = os.getenv("TMDB_TOKEN")

    if not token:
        raise RuntimeError(
            "TMDB_TOKEN no está definido"
        )

    client = TMDBClient(token)

    connection = duckdb.connect(
        str(DB_PATH)
    )

    movies = connection.execute(
        """
        SELECT
            letterboxd_id,
            name,
            year
        FROM stg_letterboxd
        ORDER BY watched_date
        """
    ).fetchall()

    for letterboxd_id, name, year in movies:

        print(
            f"Buscando: {name} ({year})"
        )

        search = client.search_movie(
            title=name,
            year=year,
        )

        results = search.get(
            "results",
            []
        )

        if not results:
            print("  ❌ No encontrado")
            continue

        movie = results[0]

        tmdb_id = movie["id"]

        print(
            f"  ✓ {movie['title']} "
            f"→ TMDB {tmdb_id}"
        )

        raw_path = (
            RAW_PATH /
            f"{tmdb_id}.json"
        )

        if raw_path.exists():

            print(
                "  ↳ RAW ya existe, "
                "saltando"
            )

            continue

        print(
            "  ↓ Descargando detalles..."
        )

        data = client.get_movie(
            tmdb_id
        )

        save_raw_movie(
            tmdb_id=tmdb_id,
            data=data,
        )

        print(
            f"  ✓ Guardado: {raw_path}"
        )


    connection.close()


if __name__ == "__main__":
    main()