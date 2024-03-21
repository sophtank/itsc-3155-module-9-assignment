from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # Feature 1:  Ashleigh Sico
    return render_template('list_all_movies.html', list_movies_active=True, movies=movie_repository.get_all_movies())


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('Mname')
    directorName = request.form.get('Dname')
    rating = int(request.form.get('rating'))
    if(rating > 0 and rating < 6):
        movie = movie_repository.create_movie(title, directorName, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    current_movie = movie_repository.get_movie_by_id(movie_id)
    if current_movie == None:
        title, director, rating = " ", " ", " "
        exists = 0
    else:
        exists = 1
        title = current_movie.title
        director = current_movie.director
        rating = current_movie.rating
    return render_template('get_single_movie.html', title=title, director=director, rating=rating, exists = exists)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
