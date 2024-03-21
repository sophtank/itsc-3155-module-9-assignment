# TODO: Feature 2
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_happy_path():
    test_app = app.test_client()

    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '4'
    }, follow_redirects = True)

    assert response.status_code == 200

    response = test_app.post('/movies', data={
        'Mname' : 'Movie',
        'Dname' : 'Director',
        'rating' : '5'
    }, follow_redirects = True)

    assert response.status_code == 200

    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 2

    assert get_movie_repository().get_movie_by_title('Test Movie') != None
    assert get_movie_repository().get_movie_by_title('wiz') == None
    assert get_movie_repository().get_movie_by_title('Movie') != None

def test_WrongInput_and_Edge():
    test_app = app.test_client()
    get_movie_repository().clear_db()

    response = test_app.post('/movies', data={
        'Mname' : 'Test Movie',
        'Dname' : 'Test Director',
        'rating' : '4'
    }, follow_redirects = True)

    assert response.status_code == 200

    response = test_app.post('/movies', data={
        'Mname' : 'Movie',
        'Dname' : 'Director',
        'rating' : '5'
    }, follow_redirects = True)

    assert response.status_code == 200

    movies = get_movie_repository().get_all_movies()
    assert len(movies) == 2

    response = test_app.post('/movies', data={
        'Mname' : 'hi',
        'Dname' : 'jack',
        'rating' : '100'
    }, follow_redirects = True)

    assert response.status_code == 200

    response = test_app.post('/movies', data={
        'Mname' : 'dog',
        'Dname' : 'mike',
        'rating' : '5'
    }, follow_redirects = True)

    assert response.status_code == 200

    assert len(movies) == 2

    assert get_movie_repository().get_movie_by_title('Test Movie') != None
    assert get_movie_repository().get_movie_by_title('wiz') == None
    assert get_movie_repository().get_movie_by_title('Movie') != None