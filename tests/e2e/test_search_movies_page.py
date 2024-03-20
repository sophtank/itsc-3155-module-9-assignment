# TODO: Feature 3

from app import app 
from src.repositories.movie_repository import get_movie_repository

def test_search_movies():
    test_app= app.test_client()

    response = test_app.post('/movies',data = {
        'Mname': 'Hunger Games',
        'Dname': 'Gary Ross', 
        'rating': '9'
    }, follow_redirects = True)

    assert response.status_code == 200


    response = test_app.post('/movies',data = {
        'Mname': 'The Matrix',
        'Dname': 'Lana Wachowski', 
        'rating': '9'
    }, follow_redirects = True)

    assert response.status_code == 200


    search_response = test_app.get('/movies/search', query_string= {'title': 'Hunger Games'})
    assert search_response.status_code ==200

    assert b'Hunger Games' in search_response.data
    assert b'Gary Ross' in search_response.data
    assert b'9' in search_response.data


    non_existing_search_response = test_app.get('/movies/search', query_string={'title': 'Diary of A Wimpy Kid'})
    assert non_existing_search_response.status_code == 200

    assert b'No Movie Found!' in non_existing_search_response.data

    assert len(get_movie_repository().get_all_movies) == 2



