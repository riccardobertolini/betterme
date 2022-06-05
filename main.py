# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
import questionary

from analytics import analytics_main
from init import database_setup
from login import welcome
from tasks import tasks_main


if __name__ == '__main__':
    database_setup()
    username = welcome()
    exit_request = 0

    while exit_request == 0:
        action = questionary.select("Please select an action", choices=[
            "Tasks",
            "Analytics",
            "Settings",
            "Logout and Exit"
        ]).ask()

        if action == "Tasks":
            tasks_main(username)
            exit_request = 0

        if action == "Analytics":
            analytics_main(username)
            exit_request = 0

        if action == "Settings":
            exit_request = 0

        if action == "Logout and Exit":
            exit_request = 1

    print("Goodbye :)")


