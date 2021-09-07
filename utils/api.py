# importing the requests library
import requests

from utils.constants import API_KEY, BASE_URL
from utils.helper import round_up, get_random_game, round_down


def get_games():
    params = {
        'key': API_KEY,
        'page_size': 40,
        'platforms': 4
    }
    url = BASE_URL + '/games'
    r = requests.get(url=url, params=params)
    data = r.json()
    return {'games': data['results']}


def get_game_by_id(game_id):
    params = {
        'key': API_KEY,
    }
    url = BASE_URL + '/games/' + game_id
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


def get_random_game_by_genre(game_id):
    genre = get_game_by_id(game_id)['genres'][0]['slug']
    return get_random_game(get_games_by_genre(genre))


def get_games_by_genre(genre):
    params = {
        'key': API_KEY,
        'page_size': 40,
        'platforms': 4,
        'genres': genre if genre else 'adventure',
    }
    url = BASE_URL + '/games'
    r = requests.get(url=url, params=params)
    data = r.json()
    return data['results']


def get_games_by_metacritic(metacritic):
    metacritic_from = round_down(metacritic) if metacritic else 90
    metacritic_to = round_up(metacritic) if metacritic else 99
    print(metacritic_from)
    print(metacritic_to)

    params = {
        'key': API_KEY,
        'page_size': 40,
        'platforms': 4,
        'metacritic': str(metacritic_from) + ',' + str(metacritic_to),
    }
    url = BASE_URL + '/games'
    r = requests.get(url=url, params=params)
    data = r.json()
    return data['results']


def get_random_game_by_metacritic(game_id):
    game = get_game_by_id(game_id)
    metacritic = game['metacritic']
    return get_random_game(get_games_by_metacritic(metacritic))


def get_recommended_games(game_id):
    games = []
    for _id in game_id:
        print(_id)
        games.append(get_random_game_by_genre(_id))
        games.append(get_random_game_by_metacritic(_id))

    return games
