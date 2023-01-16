from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import List
from middlewares import GoogleCloudContextMiddleware
from models import Movie, MovieSchema, client

app = FastAPI()

app.add_middleware(GoogleCloudContextMiddleware)

@app.get("/")
def index():
    return "ok"

@app.get("/movies/", response_model=List[MovieSchema])
def list_movies():
    movies = Movie.query().fetch()
    return jsonable_encoder([m.ser() for m in movies])

@app.post("/movies/")
def create_movie(movie: MovieSchema):
    instance = Movie(**movie.dict())
    instance.put()
    return {"message": "Movie created successfully"}

@app.get("/movies/{pk}/", response_model=MovieSchema)
def detail_movie(pk: int):
    movie = Movie.get_by_id(pk)
    print(movie)
    return movie.ser()

@app.put("/movies/{pk}/")
def update_movie(pk: int, movie: MovieSchema):
    db_movie = Movie.get_by_id(pk)
    for k,v in movie.dict().items():
        setattr(db_movie, k, v)
    db_movie.put()
    return {"message": "Movie updated successfully"}