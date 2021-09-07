import math
import random


def round_up(x):
    """Round the given number up to the nearest ten"""
    return int(math.ceil(x / 10.0)) * 10


def round_down(x):
    """Round the given number down to nearest ten"""
    return int(math.floor(x / 10.0)) * 10


def get_random_game(games):
    """Selects a random game from the given list of games"""
    return random.choice(games)
