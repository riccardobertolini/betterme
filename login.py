import sqlite3
import questionary
from typing import Callable


# todo: write comments

def validate(error_message: str) -> Callable:
    """
    Returns a function that checks if the input is both string and has a length greater than 3. If not, it prints the error message.

    :param error_message:
    :rtype Callable:
    """
    return lambda text: True if text.isalpha() and len(text) > 3 else error_message


def get_password(username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT password from users WHERE username=?""", [username])
    user_password = cursor.fetchone()
    database.close()
    return user_password[0]


def get_user_id(username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT id from users WHERE firstname=?""", [username])
    user_id = cursor.fetchone()
    database.close()
    return user_id[0]


def get_firstname(username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT firstname from users WHERE username=?""", [username])
    user_firstname = cursor.fetchone()
    database.close()
    return user_firstname[0]


def update_password(username, password):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""UPDATE users SET password=? WHERE firstname=?""", [password, username])
    affected_rows = cursor.rowcount
    database.close()
    return affected_rows > 0


def login():
    print("Welcome back!")
    print("Please type your credentials: ")

    # todo: adjust the validation

    username = questionary.text(
        "username: ",
        validate=validate("Input not valid")
        ).ask()
    password = ''
    user_credential = 'true'

    while password != user_credential:
        password = questionary.password(
            "password: ",
            validate=lambda text: True if len(text) > 3 else "Please try again"
            ).ask()
        user_credential = get_password(username)

    firstname = get_firstname(username)
    print("Welcome back, " + firstname)
    return firstname


def register_user():
    print("Welcome!")
    print("Please provide credentials to proceed.")

    # todo: adjust the validation

    username = questionary.text(
        "Please choose an username",
        validate=validate("Username not valid")
        ).ask()
    password = questionary.text(
        "Please choose a password",
        validate=lambda text: True if len(text) > 3
        else "Password not valid"
        ).ask()
    firstname = questionary.text(
        "Please choose a firstname",
        validate=validate("Firstname not valid")
        ).ask()
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()

    # todo: test if there's already this user
    userdata = [str(username), str(firstname), str(password)]
    cursor.execute("""INSERT INTO users(username, firstname, password) VALUES (?,?,?)""", userdata)
    database.commit()
    if cursor.rowcount > 0:
        print(f"Welcome {firstname}!")
    else:
        print("Sorry there's a problem. Try again please.")
    database.close()
    return firstname


def welcome():
    print("---WELCOME to BetterMe!---")
    action = questionary.select(
        "Please select an user action", choices=[
            "Login",
            "Create new user"
            ]
        ).ask()

    if action == "Login":
        username = login()
    else:
        username = register_user()

    return username
