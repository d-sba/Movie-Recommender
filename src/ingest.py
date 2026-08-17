from pathlib import Path

import duckdb


ROOT = Path(__file__).resolve().parents[1]

DB_PATH = ROOT / "db" / "movies.duckdb"

SQL_FILES = [
    ROOT / "sql" / "01_staging.sql",
    ROOT / "sql" / "02_tmdb_staging.sql",
]


def main():

    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = duckdb.connect(
        str(DB_PATH)
    )

    try:

        for sql_file in SQL_FILES:

            print(
                f"Ejecutando: {sql_file.name}"
            )

            sql = sql_file.read_text(
                encoding="utf-8"
            )

            connection.execute(sql)

        print()
        print("Tablas:")

        print(
            connection.execute(
                "SHOW TABLES"
            ).fetchdf()
        )

    finally:

        connection.close()


if __name__ == "__main__":
    main()