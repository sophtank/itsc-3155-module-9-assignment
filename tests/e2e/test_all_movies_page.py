# Feature 1:  Ashleigh Sico
from flask.testing import FlaskClient
from app import movie_repository

def test_all_movies_page(test_app: FlaskClient):
    #there are no movies in the list
    assert movie_repository.get_all_movies() == {}
    #generate a resonse
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    #verify correct status
    assert response.status_code == 200
    #verify correct HTML:  no table, correct heading
    assert '''<table>''' not in response_data
    assert '''<h1>There currently no movies.</h1>''' in response_data
