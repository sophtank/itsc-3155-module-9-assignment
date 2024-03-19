# Feature 1:  Ashleigh Sico
from src.repositories.movie_repository import get_movie_repository

#setup
movie_repository = get_movie_repository()

#test when no movies are in list
def test_get_all_movies_empty():
    #assert that get_all_movies returns an empty dictionary
    assert movie_repository.get_all_movies() == {}


#test when there are movies in list
def test_get_all_movies():
    #add some movies
    movie_repository.create_movie("My Movie", "Ashleigh Sico", "5")
    movie_repository.create_movie("Another Movie", "John Doe", "3")
    #verify that there are two movies in the list
    assert len(movie_repository.get_all_movies()) == 2
    #verify that movies are correct in the list
    id = list(movie_repository.get_all_movies().keys())[0]
    assert movie_repository.get_all_movies().get(id).title == "My Movie"
    assert movie_repository.get_all_movies().get(id).director == "Ashleigh Sico"
    assert movie_repository.get_all_movies().get(id).rating == "5"
    #the second movie
    id = list(movie_repository.get_all_movies().keys())[1]
    assert movie_repository.get_all_movies().get(id).title == "Another Movie"
    assert movie_repository.get_all_movies().get(id).director == "John Doe"
    assert movie_repository.get_all_movies().get(id).rating == "3"
