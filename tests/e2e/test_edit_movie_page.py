# TODO: Feature 5
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository


def test_edit_movie_page(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.create_movie("Life of Pi", "Ang Lee", 5)
    id = movie_repo.get_movie_by_title("Life of Pi")


    response = test_app.get(f"/movies/{id}/edit")
    response_data = response.data.decode('utf-8')

    assert response.status_code == 404