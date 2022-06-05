import sqlite3
from datetime import datetime
import questionary

from login import get_user_id


def date_today():
    return datetime.now().strftime("%Y%m%d")


class TaskClass:
    def __init__(self, name, user, periodicity):
        self.name = str(name)
        self.user = str(user),
        self.periodicity = str(periodicity),
        self.date = date_today()


def tasks_main(username):
    exit_tasks_request = 0
    while exit_tasks_request == 0:
        tasks_action = questionary.select("Select an option: ", choices=[
            "Mark completed task",
            "Create new task",
            "< Back to Main Menu"
        ]).ask()

        if tasks_action == 'Mark completed task':
            exit_mark_task_done = 0
            while exit_mark_task_done == 0:
                task_name = questionary.text("Name the task you completed: ").ask()
                completed_updated = complete_task(task_name, username)
                if completed_updated == 1:
                    print(task_name + " marked as completed!")
                    exit_mark_task_done = 1
                else:
                    print("Problem, try again")

        if tasks_action == 'Create new task':
            task_name = questionary.text("Please write task name:").ask()
            tasks_periodicity = questionary.select("Select an option: ", choices=[
                "monthly",
                "weekly",
                "daily"
            ]).ask()
            create_new_task(task_name, username, tasks_periodicity)
            ##todo: check if task is created

            print("Task " + task_name + " created!")

        tasks_menu_action = questionary.confirm("< Back to Main Menu").ask()

        if tasks_menu_action:
            exit_tasks_request = 1


def create_new_task(name, user, periodicity):
    task = TaskClass(name, user, periodicity)

    database = sqlite3.connect('./database.db')
    cursor = database.cursor()

    taskdata = [task.name, get_user_id(task.user[0]), task.periodicity[0], task.date]
    cursor.execute("""INSERT INTO tasks(name, user, periodicity, date) VALUES (?,?,?,?)""", taskdata)
    database.commit()
    database.close()


def complete_task(task_name, username):
    database = sqlite3.connect('./database.db')
    cursor = database.cursor()

    cursor.execute("""SELECT id FROM tasks WHERE name=?""", [task_name])
    task_id = cursor.fetchone()
    if task_id:
        progressdata = [task_id[0], get_user_id(username), datetime.now(), ]
        cursor.execute("""INSERT INTO progresses(taskId, user, date) VALUES (?,?,?)""", progressdata)
        database.commit()
        database.close()

        return 1
    else:
        return 0
