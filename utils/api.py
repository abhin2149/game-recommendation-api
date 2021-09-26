import requests
from db.db import sql_connection, create_table, insert_into_table, fetch_from_table
from utils.constants import API_KEY, BASE_URL, IMAGE_API_KEY, IMAGE_SEARCH_URL
from utils.helper import round_up, round_down, get_genres, get_games_per_genre, get_random_games, format_games, \
    get_random_page


def get_game_by_id(game_id):
    """Retrieve a game using the unique id"""
    params = {
        'key': API_KEY,
    }
    url = BASE_URL + '/games/' + game_id
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


def get_games_by_genre(genre):
    """Retrieve all the games belonging to a genre"""
    page = get_random_page()
    params = {
        'key': API_KEY,
        'page': page,
        'page_size': 40,
        'platforms': 4,
        'genres': genre if genre else 'action',
    }
    url = BASE_URL + '/games'
    r = requests.get(url=url, params=params)
    data = r.json()
    return data['results']


def get_random_games_by_genres(game_ids):
    """Main function to get random games by each genre"""
    genres = set()
    original_games = []
    for _id in game_ids:
        cur_game = get_game_by_id(_id)
        original_games.append(cur_game)
        genres_object = cur_game['genres']
        new_genres = get_genres(genres_object)
        for genre in new_genres:
            genres.add(genre)

    games_per_genre = get_games_per_genre(genres)
    games = []
    for genre in genres:
        games += get_random_games(get_games_by_genre(genre), games_per_genre, original_games)
    return games


def get_games_by_metacritic(metacritic, genre):
    """Retrieve games between a given metacritic range"""
    metacritic_from = round_down(metacritic) if metacritic else 90
    metacritic_to = round_up(metacritic) if metacritic else 99
    params = {
        'key': API_KEY,
        'page_size': 40,
        'platforms': 4,
        'genres': genre if genre else 'adventure',
        'metacritic': str(metacritic_from) + ',' + str(metacritic_to),
    }
    url = BASE_URL + '/games'
    r = requests.get(url=url, params=params)
    data = r.json()
    return data['results']


def get_recommended_games(game_ids):
    """Driver function to get recommended games"""
    return get_random_games_by_genres(game_ids)


def get_image_search_data(url):
    """Retrieve image analysis result"""
    params = {
        'engine': 'google_reverse_image',
        'image_url': url,
        'api_key': IMAGE_API_KEY,
    }
    url = IMAGE_SEARCH_URL
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


def save_liked_games(_id, name, rating, date):
    """Save liked games to sqlite DB"""
    con = sql_connection()
    create_table(con)
    game = {
        'id': _id,
        'name': name,
        'rating': rating,
        'date': date,
    }
    insert_into_table(game, con)


def get_liked_games():
    """Retrieve liked games from sqlite Db"""
    con = sql_connection()
    games_sql = fetch_from_table(con)
    games = format_games(games_sql)
    return games

