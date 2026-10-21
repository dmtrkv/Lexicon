from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def main():
    return {"message": "🍿"}


movies = [
    {"id": 1, "title": "The Clockwork Moon",
        "director": "Elena Voss", "year": 2021},
    {"id": 2, "title": "Whispers Beneath the Ocean",
        "director": "Marcus Vale", "year": 2018},
    {"id": 3, "title": "The Last Lighthouse on Mars",
        "director": "Amara Quinn", "year": 2023},
    {"id": 4, "title": "A Kingdom Made of Shadows",
        "director": "Oliver Wren", "year": 2020},
]


def find_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

# @app.get("/movies")
# def get_movies():
#     return movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)


@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    result = movies
    if director:
        result = [movie for movie in result if director.lower()
                  in movie["director"].lower()]
    if year:
        result = [movie for movie in result if year == movie["year"]]
    return result


class Movie(BaseModel):
    title: str
    director: str
    year: int


@app.post("/movies", status_code=201)
def add_movie(movie: Movie):
    new_id = max(m["id"] for m in movies) + 1
    new_movie = {
        "id": new_id,
        "title": movie.title,
        "director": movie.director,
        "year": movie.year
    }
    movies.append(new_movie)
    return new_movie


@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updated_movie: Movie):
    movie = find_movie(movie_id)
    movie["title"] = updated_movie.title
    movie["director"] = updated_movie.director
    movie["year"] = updated_movie.year
    return movie


@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


@app.patch("/movies/{movie_id}")
def partial_movie_update(movie_id: int, movie_update: MovieUpdate):
    movie = find_movie(movie_id)
    movie.update(movie_update.model_dump(exclude_unset=True))
    return movie


# 2 Test that only one field changes
# In /docs, send a body that only contains {"year": 2000}. Check with GET /movies/1
# that the title and the director are unchanged.
pass

# 3 Test the edges
# What happens with an empty body {}? And with a year written as text ('abc')? And with an id
# that does not exist? Write down the status code for each.
# 200, 422, 404

# 4 Explain the difference
# Write two sentences, as a comment in your code, about when you would use PUT and
# when you would use PATCH.
# PUT - updating all fields (i.e. replacing entity)
# PATCH - updating particular fields
