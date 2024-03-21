# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository


def test_search_movies():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    
    movie_repo.create_movie("Hunger Games", "Gary Ross", 4)
    movie_repo.create_movie("The Matrix", "Lana Wachowski", 5)

    search_result = movie_repo.get_movie_by_title("Hunger Games")
    assert search_result is not None
    assert search_result.title == "Hunger Games"
    assert search_result.director == "Gary Ross"
    assert search_result.rating == 4

    non_existing_search_result = movie_repo.get_movie_by_title("Diary of A Wimpy Kid")
    assert non_existing_search_result is None
