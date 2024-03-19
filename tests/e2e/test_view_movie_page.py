from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_movies_empty(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    response = test_app.get('/movies/200')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1>There is no movie with the given ID.</h1>' in response_data

def test_jurassic_example(test_app: FlaskClient):
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    my_movie = movie_repo.create_movie("Jurassic Park", "Steven Spielberg", 5)
    my_id = my_movie.movie_id
    response = test_app.get(f'/movies/{my_id}')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    assert '<h1>Jurassic Park</h1>' in response_data
    assert '<h2>Directed by Steven Spielberg.</h2>' in response_data
    assert '<p>You rated this movie a 5 out of 5.</p>' in response_data