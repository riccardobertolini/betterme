import sqlite3
import questionary
from login import update_password

from datetime import datetime

'''
Setting page functions. Taking care mainly of updating user's password, could be extended in future
'''

def settings_main(username: str):
    exit_analytics_request = 0
    while exit_analytics_request == 0:
        analytics_action = questionary.select(
            "Select an option: ", choices=[
                "Change Password",
                "< Back to Main Menu"
                ]
            ).ask()

        if analytics_action == 'Change Password':
            new_password = questionary.text(
                "Please choose a new password",
                validate=lambda text: True if len(text) > 3
                else "Password too short"
                ).ask()
            result = update_password(username, new_password)
            if result:
                print('Password updated!')
            else:
                print('There is an error, try again.')

        if analytics_action == '< Back to Main Menu':
            analytics_menu_action = questionary.confirm("< Back to Main Menu").ask()
            print(analytics_menu_action)
            if analytics_menu_action:
                exit_analytics_request = 1
