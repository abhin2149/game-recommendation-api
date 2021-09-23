import math
import random

from utils.constants import GAMES_COUNT


def round_up(x):
    """Round the given number up to the nearest ten"""
    return int(math.ceil(x / 10.0)) * 10


def round_down(x):
    """Round the given number down to nearest ten"""
    return int(math.floor(x / 10.0)) * 10


def get_random_games(games, n, original_games):
    """Selects n random games from the given list of games"""

    # first remove the original games that user has already selected
    for game_o in original_games:
        for game in games:
            if game_o['id'] == game['id']:
                games.remove(game)

    return random.sample(games, n)


def get_genres(genres_object):
    """Cleans the genres object and extracts the required details"""
    genres = []
    for genre in genres_object:
        genres.append(genre['slug'])

    return genres


def get_games_per_genre(genres):
    return int(math.ceil(GAMES_COUNT / len(genres)))

