import sqlite3
import questionary


def get_password(username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT password from users WHERE username=?""", [username])
    user_password = cursor.fetchone()
    database.close()
    return user_password[0]


def get_firstname(username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()
    cursor.execute("""SELECT firstname from users WHERE username=?""", [username])
    user_firstname = cursor.fetchone()
    database.close()
    return user_firstname[0]


def login():
    print("Welcome back!")
    print("Please type your credentials: ")
    username = questionary.text("username: ",
                                validate=lambda text: True if text.isalpha() and len(
                                    text) > 3 else "Input not valid").ask()
    password = ''
    user_credential = 'true'

    while password != user_credential:
        password = questionary.password("password: ",
                                        validate=lambda text: True if len(text) > 3 else "Please try again").ask()
        user_credential = get_password(username)

    firstname = get_firstname(username)
    print("Welcome back, " + firstname)


def register_user():
    print("Welcome!")
    print("Please provide credentials to proceed.")
    username = questionary.text("Please choose an username",
                                validate=lambda text: True if text.isalpha() and len(text) > 3
                                else "Username not valid").ask()
    password = questionary.text("Please choose a password",
                                validate=lambda text: True if len(text) > 3
                                else "Password not valid").ask()
    firstname = questionary.text("Please choose a firstname",
                                 validate=lambda text: True if text.isalpha() and len(text) > 3
                                 else "Firstname not valid").ask()
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


def welcome():
    print("---WELCOME!---")
    action = questionary.select("Please select an user action", choices=[
        "Login",
        "Create new user"
    ]).ask()

    if action == "Login":
        login()
    else:
        register_user()
