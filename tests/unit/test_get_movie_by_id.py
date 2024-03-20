# TODO: Feature 4
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_movies_empty():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    assert movie_repo.get_all_movies() == {}

def test_make_movie():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    my_movie = movie_repo.create_movie("Jurassic Park", "Steven Spielberg", 5)
    my_id = my_movie.movie_id
    assert my_movie.title == "Jurassic Park"
    assert my_movie.director == "Steven Spielberg"
    assert my_movie.rating == 5