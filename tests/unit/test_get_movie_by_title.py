# TODO: Feature 3
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_search_movie_found():
    test_app = app.test_client()
    get_movie_repository().clear_db()


    test_app.post('/movies', data = {
        'Mname': 'Test Movie',
        'Dname': 'Test Director',
        'Rating' : 6

    }, follow_redirects = True)


    response = test_app.get('/movies/search', query_string = {'title':'Test Movie', 'rating': '4'})

    assert response.status_code ==200
    assert b'Test Movie' in response.data
    assert b'Test Director' in response.data
    assert b'4' in response.data

def test_search_movie_not_found():
    test_app = app.test_client()
    get_movie_repository().clear_db()
    response = test_app.get ('/movies/search', query_string = {'title' : 'Nonexistent Movie'})

    assert response.status_code ==200


def test_search_movie_empty_title():
    test_app = app.test_client()
    get_movie_repository().clear_db()


    test_app.post ('/movies', data = {
        'Mname': 'Test Movie',
        'Dnmae': 'Test Director',
        'rating': 9

    }, follow_redirects = True)

    response = test_app.get('/movies/search', query_string = {'title': " "})
    
    assert response.status_code==200



