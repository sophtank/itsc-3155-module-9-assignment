# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_search_movie_not_found(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()

    response = test_app.get('/movies/search?title=nonexistent movie')
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert 'Movie Not Found' in response_data


def test_search_movie_found(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_repo.create_movie("the matrix", "Lana Wachowski", 9)

    response = test_app.get('/movies/search?title=the matrix')
    assert response.status_code == 200

    response_data = response.data.decode('utf-8')
    assert 'the matrix' in response_data
    assert 'Lana Wachowski' in response_data
    assert '9' in response_data


def test_search_movie_special_characters(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_repo.create_movie("the lord of the rings: the fellowship of the ring", "Peter Jackson", 8)

    response = test_app.get('/movies/search?title=the lord of the rings: the fellowship of the ring')
    assert response.status_code == 200

    response_data = response.data.decode('utf-8')
    assert 'the lord of the rings: the fellowship of the ring' in response_data
    assert 'Peter Jackson' in response_data
    assert '8' in response_data
