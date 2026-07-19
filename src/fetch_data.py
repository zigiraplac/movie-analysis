import requests
from config import API_KEY, BASE_URL
import pandas as pd
import time

def fetch_movie(movie_id):
    res = requests.get(f"{BASE_URL}/movie/{movie_id}", params={"api_key": API_KEY})

    if res.status_code != 200:
        return {
            "status_code": res.status_code,
            "message": res.json().get("status_message"),
        }

    details = res.json()

    credits_res = requests.get(
        f"{BASE_URL}/movie/{movie_id}/credits", params={"api_key": API_KEY}
    )

    if credits_res.status_code == 200:
        credits = credits_res.json()
    else:
        credits = {"cast": [], "crew": []}

    # pull director from crew list
    directors = [c["name"] for c in credits.get("crew", []) if c["job"] == "Director"]
    director = directors[0] if directors else None

    details["cast"] = credits.get("cast", [])
    details["cast_size"] = len(credits.get("cast", []))
    details["director"] = director
    details["crew_size"] = len(credits.get("crew", []))
    details["status_code"] = res.status_code
    return details


def fetch_movies(movie_ids):

    movies = []

    for index, movie_id in enumerate(movie_ids, start=1):

        print(f"Fetching {index}/{len(movie_ids)}")

        movie = fetch_movie(movie_id)

        if movie.get("status_code") == 200:
            movies.append(movie)

        time.sleep(0.25)

    return pd.DataFrame(movies)
