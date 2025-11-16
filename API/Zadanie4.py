import csv
import json

from starlette.responses import PlainTextResponse

from Zadanie1 import app
from Zadanie3 import Link, Rating, Tag



def load_links():
    links = []
    with open("links.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            link = Link(
                row["movieId"],
                row["imdbId"],
                row["tmdbId"]
            )
            links.append(link.__dict__)
    return links


def load_ratings():
    ratings = []
    with open("ratings.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rating = Rating(
                row["userId"],
                row["movieId"],
                row["rating"],
                row["timestamp"]
            )
            ratings.append(rating.__dict__)
    return ratings


def load_tags():
    tags = []
    with open("tags.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tag = Tag(
                row["userId"],
                row["movieId"],
                row["tag"],
                row["timestamp"]
            )
            tags.append(tag.__dict__)
    return tags



@app.get("/links", response_class=PlainTextResponse)
def get_links():
    links = load_links()
    lines = [json.dumps(link, ensure_ascii=False) for link in links]
    return "\n".join(lines)


@app.get("/ratings", response_class=PlainTextResponse)
def get_ratings():
    ratings = load_ratings()
    lines = [json.dumps(rating, ensure_ascii=False) for rating in ratings]
    return "\n".join(lines)


@app.get("/tags", response_class=PlainTextResponse)
def get_tags():
    tags = load_tags()
    lines = [json.dumps(tag, ensure_ascii=False) for tag in tags]
    return "\n".join(lines)
