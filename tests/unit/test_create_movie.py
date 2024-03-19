# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository 


def test_send_to_database():
    test_app = app.test_client()

    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '4'
    }, follow_redirects = True)

    assert response.status_code == 200


def test_add_to_database():
    test_app = app.test_client()
    get_movie_repository().clear_db()
    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '4'
    }, follow_redirects = True)
    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 1

def test_no_movies_added():
    get_movie_repository().clear_db()
    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 0


def test_wrong_input():
    test_app = app.test_client()
    get_movie_repository().clear_db()
    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '9'
    }, follow_redirects = True)
    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 0

def test_multiple_inputs():
    test_app = app.test_client()
    get_movie_repository().clear_db()
    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '4'
    }, follow_redirects = True)

    response = test_app.post('/movies', data={
        'Mname' : ' Movie',
        'Dname' : ' Director',
        'rating' : '1'
    }, follow_redirects = True)
    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 2