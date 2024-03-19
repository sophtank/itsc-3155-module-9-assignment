# Feature 1:  Ashleigh Sico
from flask.testing import FlaskClient
from app import movie_repository

def test_all_movies_page_empty(test_app: FlaskClient):
    movie_repository.clear_db()
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

def test_all_movies_page(test_app: FlaskClient):
    movie_repository.clear_db()
    #add some movies
    movie_repository.create_movie("My Movie", "Ashleigh Sico", "5")
    movie_repository.create_movie("Another Movie", "John Doe", "3")
    #generate a response
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    #verify correct status
    assert response.status_code == 200
    #verify correct HTML:  table with movies
    assert '''<tr>
        <td>My Movie</td>
        <td>Ashleigh Sico</td>
        <td>5</td>
    </tr>''' in response_data
    assert '''<tr>
        <td>Another Movie</td>
        <td>John Doe</td>
        <td>3</td>
    </tr>''' in response_data
    assert '''<h1>There currently no movies.</h1>''' not in response_data