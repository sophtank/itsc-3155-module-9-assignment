# TODO: Feature 5
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()
movie = movie_repository.create_movie("Life of Pi", "Ang Lee", 5)

def test_edit_movie_page(test_app: FlaskClient):
    id = movie_repository.get_movie_by_title("Life of Pi").movie_id

    response = test_app.get(f"/movies/{id}/edit")
    response_data = response.data.decode('utf-8')

    assert response.status_code == 200


def test_edited_movie_page(test_app: FlaskClient):
    response = test_app.post(f"/movies/{movie.movie_id}", data ={
        "title" : "Star Wars",
        "director" : "George Lucas",
        "rating" : "4"
        }, follow_redirects=True)
    
    assert response.status_code == 200
    
    assert movie.title == "Star Wars"
    assert movie.director == "George Lucas"
    assert movie.rating == "4"
