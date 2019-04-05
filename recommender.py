
import random

MOVIES = [
    "Shawshank Redemption",
    "The Martian",
    "Mean Girls",
    "Star Trek (all of them)",
    "The Usual Suspects"
]

def recommend():
    movie = random.sample(MOVIES, 1)
    return movie


print(recommend())
