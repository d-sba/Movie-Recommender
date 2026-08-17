import requests


class TMDBClient:

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, token: str):
        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "accept": "application/json",
        })

    def search_movie(self, title: str, year: int | None = None):

        params = {
            "query": title,
            "include_adult": "false",
        }

        if year:
            params["primary_release_year"] = year

        response = self.session.get(
            f"{self.BASE_URL}/search/movie",
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def get_movie(self, tmdb_id: int):
        params = {
            "append_to_response": (
                "credits,"
                "external_ids,"
                "keywords,"
                "videos,"
                "release_dates"
            )
        }

        response = self.session.get(
            f"{self.BASE_URL}/movie/{tmdb_id}",
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()