from Zadanie1 import app
from fastapi.responses import PlainTextResponse
import json

class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = int(movieId)
        self.title = title
        self.genres = genres

import csv

def load_movies():
    movies = []
    with open("movies.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie = Movie(
                movieId=row["movieId"],
                title=row["title"],
                genres=row["genres"]
            )
            movies.append(movie.__dict__)  # serializacja
    return movies

@app.get("/movies", response_class=PlainTextResponse)
def get_movies():
    movies = load_movies()
    lines = [json.dumps(movie, ensure_ascii=False) for movie in movies]
    return "\n".join(lines)