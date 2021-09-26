import sqlite3

from sqlite3 import Error


def sql_connection():
    """Connect to the local db file"""
    try:
        connection = sqlite3.connect('games.db')
        return connection

    except Error:
        print(Error)


def create_table(connection):
    """Create games table to store liked games by user"""
    cursor_obj = connection.cursor()
    cursor_obj.execute("CREATE TABLE IF NOT EXISTS games(id integer PRIMARY KEY, name text, rating real, launchDate text)")
    connection.commit()


def insert_into_table(values, connection):
    """Insert liked games by user into the table"""
    cursor_obj = connection.cursor()
    entities = (values['id'], values['name'], values['rating'], values['date'])
    cursor_obj.execute('INSERT INTO games(id, name, rating, launchDate) VALUES(?, ?, ?, ?)', entities)
    connection.commit()


def fetch_from_table(connection):
    """Fetch liked games from the games table"""
    cursor_obj = connection.cursor()
    cursor_obj.execute('SELECT * FROM games')
    rows = cursor_obj.fetchall()
    games = []
    for row in rows:
        games.append(row)
    return games
