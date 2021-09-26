import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        connection = sqlite3.connect('games.db')
        return connection

    except Error:
        print(Error)


def create_table(connection):
    cursor_obj = connection.cursor()
    cursor_obj.execute("CREATE TABLE IF NOT EXISTS games(id integer PRIMARY KEY, name text, rating real, launchDate text)")
    connection.commit()


def insert_into_table(values, connection):
    cursor_obj = connection.cursor()
    entities = (values['id'], values['name'], values['rating'], values['date'])
    cursor_obj.execute('INSERT INTO games(id, name, rating, launchDate) VALUES(?, ?, ?, ?)', entities)
    connection.commit()


def fetch_from_table(connection):
    cursor_obj = connection.cursor()
    cursor_obj.execute('SELECT * FROM games')
    rows = cursor_obj.fetchall()
    games = []
    for row in rows:
        games.append(row)
    return games


# con = sql_connection()
# create_table(con)
#
# game = {
#     'id': 2,
#     'name': 'Game',
#     'rating': 3.55,
#     'date': '2-3-21',
# }
#
# insert_into_table(game, con)
# games = fetch_from_table(con)
#
# for game_obj in games:
#     print(game_obj[0])
