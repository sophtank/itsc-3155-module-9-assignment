# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_search_movie_not_found(test_app: FlaskClient):
    movie_repo =get_movie_repository()
    movie_repo.clear_db()
    response = test_app.get('/movies/search?title=Nonexistient Movie')
    response_data = response.data.decode('utf-8')
    assert response.status_code ==200
    assert 'Movie Not Found' in response_data


