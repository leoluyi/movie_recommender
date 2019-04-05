
from movie_recommender.movie_recommender import recommend, MOVIES

def test_valid_movie():
    """The recommended movie is in the list of movies."""
    movie = recommend()
    assert movie in MOVIES

def test_string_movie():
    """recommended movies are strings"""
    movie = recommend()
    assert type(movie) == str
