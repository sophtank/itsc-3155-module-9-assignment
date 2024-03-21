# TODO: Feature 5
from src.models.movie import Movie
from flask.testing import FlaskClient
from app import app



def test_update_movie():
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)

    assert type(movie) == Movie
    assert movie.movie_id == 123
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5

    movie.title = 'Life of Pi'
    movie.director = 'Ang Lee'
    movie.rating = 4
    
    assert movie.movie_id == 123
    assert movie.title == 'Life of Pi'
    assert movie.director == 'Ang Lee'
    assert movie.rating == 4
