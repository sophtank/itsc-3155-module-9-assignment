# TODO: Feature 6

from app import app
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie():
    test_app = app.test_client()
    


    movies = get_movie_repository()

    movies.clear_db()

    movie1 = movies.create_movie("Movie1", "Director1", 1)
    movie2 = movies.create_movie("Movie2", "Director2", 2)
    movie3 = movies.create_movie("Movie3", "Director3", 3)

    assert len(movies.get_all_movies()) == 3

    movie2id = movie2.movie_id

    movies.delete_movie(movie2id)

    assert len(movies.get_all_movies()) == 2
