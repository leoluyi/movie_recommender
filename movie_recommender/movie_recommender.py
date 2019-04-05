
import random

MOVIES = [
    "Shawshank Redemption",
    "The Martian",
    "Mean Girls",
    "Star Trek (all of them)",
    "The Usual Suspects"
]

def recommend():
    """Recommends one movie"""
    movie = random.sample(MOVIES, 1)
    return movie[0]
    #movie = str(random.sample(MOVIES, 1))
    #return movie[2:-2]
    #return random.choice(MOVIES)


print(recommend())
