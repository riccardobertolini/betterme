import sqlite3
from datetime import datetime
import questionary


class Task:
    def __init__(
        self, t_id: int, name: str, user: str, periodicity: str, date: str = datetime.now().strftime("%Y%m%d")
        ):
        self.id = t_id
        self.name = name
        self.user = user
        self.periodicity = periodicity
        self.date = date

    def complete(self, dbpath: str):
        """
        Complete the task
        :return:
        :rtype:
        """
        database = sqlite3.connect(dbpath)
        cursor = database.cursor()
        progressdata = [self.id, self.user, self.date]
        cursor.execute("""INSERT INTO progresses(taskId, user, date) VALUES (?,?,?)""", progressdata)
        database.commit()
        database.close()


class TaskManager:
    def __init__(self, user: str, dbpath="./database.db"):
        self.cached_tasks: dict[str, Task] = {}
        self.user = user
        self.dbpath = dbpath

    def get_task(self, task_name: str):
        '''
        Checks if the task has been retrieved from the database. If not, it retrieves it from the database.

        :param task_name:
        :rtype Task:
        '''
        if task_name in self.cached_tasks:
            return self.cached_tasks[task_name]

        database = sqlite3.connect(self.dbpath)
        cursor = database.cursor()
        cursor.execute("""SELECT id,name,periodicity,date FROM tasks WHERE name=? AND user=?""", [task_name, self.user])
        tast = cursor.fetchone()
        if tast is None:
            return None
        task = Task(tast[0], tast[1], self.user, tast[2], tast[3])
        self.cached_tasks.update({task_name: task})
        database.commit()
        database.close()
        return self.cached_tasks[task_name]

    def create_task(self, task_name: str, periodicity: str) :
        """
        Creates a task, caches the task then returns the task object
        :param task_name:
        :type task_name:
        :param periodicity:
        :type periodicity:
        :return task object:
        :rtype Task:
        """
        task = self.get_task(task_name)

        if task is not None:
            print("Task already exists")
            return None

        database = sqlite3.connect(self.dbpath)
        cursor = database.cursor()

        taskdata = [task_name, self.user, periodicity, datetime.now().strftime("%Y%m%d")]
        cursor.execute("""INSERT INTO tasks(name, user, periodicity, date) VALUES (?,?,?,?)""", taskdata)
        database.commit()
        database.close()
        return self.get_task(task_name)

    def complete_task(self, task_name) -> int:
        """
        Gets the task and then calls the complete method on the task object
        :param task_name:
        :type task_name:
        :rtype int:
        """
        task = self.get_task(task_name)
        if task is None:
            return 0
        task.complete(self.dbpath)
        return 1

    def main(self):
        exit_tasks_request = 0
        while exit_tasks_request == 0:
            tasks_action = questionary.select(
                "Select an option: ", choices=[
                    "Mark completed task",
                    "Create new task",
                    "< Back to Main Menu"
                    ]
                ).ask()

            if tasks_action == 'Mark completed task':
                exit_mark_task_done = 0
                while exit_mark_task_done == 0:
                    task_name = questionary.text("Name the task you completed: ").ask()
                    completed_updated = self.complete_task(task_name)
                    if completed_updated == 1:
                        print(task_name + " marked as completed!")
                        exit_mark_task_done = 1
                    else:
                        print("Problem, try again")

            if tasks_action == 'Create new task':
                task_name = questionary.text("Please write task name:").ask()
                tasks_periodicity = questionary.select(
                    "Select an option: ", choices=[
                        "monthly",
                        "weekly",
                        "daily"
                        ]
                    ).ask()
                self.create_task(task_name, tasks_periodicity)
                ##todo: check if task is created
                print("Task " + task_name + " created!")

            tasks_menu_action = questionary.confirm("< Back to Main Menu").ask()

            if tasks_menu_action:
                exit_tasks_request = 1
