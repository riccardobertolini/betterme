import sqlite3


def database_setup(database='./database.db'):
    database = sqlite3.connect(database)
    cursor = database.cursor()

    print('Database check...')
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username text,
            firstname text,
            password text
            )"""
        )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS progresses (
            id INTEGER PRIMARY KEY,
            taskId text,
            user int,
            date TIMESTAMP
            )"""
        )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name text,
            user text,
            date TIMESTAMP,
            periodicity text
            )"""
        )

    print('Done')

    cursor.close()

# Todo: add test tasks
