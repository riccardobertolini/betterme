import os
import unittest
import sqlite3
from init import database_setup
from tasks import TaskManager, Task


class TestTask(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        with open("test.db", "w") as f:
            pass
        self.dbpath = './test.db'
        self.db = sqlite3.connect(self.dbpath)
        database_setup(self.dbpath)

        self.user = "test"
        cursor = self.db.cursor()
        userdata = [self.user, "test", "test"]
        cursor.execute("""INSERT INTO users(username, firstname, password) VALUES (?,?,?)""", userdata)
        self.db.commit()

        self.tskmngr = TaskManager(self.user, self.dbpath)

    @classmethod
    def tearDownClass(self) -> None:
        self.db.close()
        os.remove(self.dbpath)

    def test_1_create_task(self):
        created_task = self.tskmngr.create_task("test_task", "monthly")
        self.assertIsInstance(created_task, Task)
        self.assertEqual(created_task.id, 1)
        self.assertEqual(created_task.name, "test_task")
        self.assertEqual(created_task.periodicity, "monthly")

    def test_2_get_task(self):
        got_task = self.tskmngr.get_task("test_task")
        self.assertIsInstance(got_task, Task)
        self.assertEqual(got_task.id, 1)
        self.assertEqual(got_task.name, "test_task")
        self.assertEqual(got_task.periodicity, "monthly")

    def test_3_complete_task(self):
        completed = self.tskmngr.complete_task("test_task")
        self.assertEqual(completed, 1)

        cursor = self.db.cursor()
        task = self.tskmngr.get_task("test_task")
        cursor.execute("""SELECT taskId FROM progresses WHERE taskId=?""", [task.id])
        self.assertEqual(cursor.fetchone()[0], str(task.id))


if __name__ == '__main__':
    unittest.main()
