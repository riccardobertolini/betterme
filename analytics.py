import sqlite3
import questionary
from login import get_user_id
from tasks import date_today


def analytics_main(username):
    exit_analytics_request = 0
    while exit_analytics_request == 0:
        analytics_action = questionary.select("Select an option: ", choices=[
            "Show completed task today",
            "Show longest steak for a task",
            "Show longest steak ever",
            "< Back to Main Menu"
        ]).ask()

        if analytics_action == 'Show completed task today':
            database = sqlite3.connect('./database.db')
            cursor = database.cursor()

            userId = get_user_id(username)
            today = date_today()
            cursor.execute("""SELECT * from progresses WHERE date >= ? AND user=?""", [today, userId])
            tasks_list = cursor.fetchall()

            print("Tasks completed today:")
            for singleTask in tasks_list:
                cursor.execute("""SELECT name from tasks WHERE id = ?""", [singleTask[1]])
                task_name = cursor.fetchone()
                print(task_name[0])

                database.close()

        if analytics_action == 'Show longest steak for a task':
            questionary.text("")

        if analytics_action == 'Show longest steak ever':
            database = sqlite3.connect('./database.db')
            cursor = database.cursor()
            cursor.execute("""SELECT taskId, count(*) from progresses GROUP BY taskId ORDER BY count(*) DESC""")
            highest_steak_entry = cursor.fetchone()

            if highest_steak_entry:
                cursor.execute("""SELECT name from tasks WHERE id = ?""", [highest_steak_entry[0]])
                highest_steak = cursor.fetchone()

            print('The highest steak ever is with this task: ' + highest_steak[0] + ' completed ' + str(highest_steak_entry[1]) + ' times!')
            database.close()

        if analytics_action == '< Back to Main Menu':
            analytics_menu_action = questionary.confirm("< Back to Main Menu").ask()
            print(analytics_menu_action)
            if analytics_menu_action:
                exit_analytics_request = 1
