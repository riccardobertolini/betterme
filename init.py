import sqlite3


def database_setup():
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()

    print('Database check...')
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id int PRIMARY KEY AUTOINCREMENT,
    username text,
    firstname text,
    password text
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS progresses (
    id int PRIMARY KEY AUTOINCREMENT,
    taskId text,
    completed int,
    eventDate string
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id int PRIMARY KEY AUTOINCREMENT,
    taskName text,
    periodicity text
    )""")

    print('Done')

    cursor.close()

#Todo: add test tasks