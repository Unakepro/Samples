import sqlite3
import os


class MyDatabaseManager:

    def __init__(self, data_name):
        self._data_name = data_name

    def __enter__(self):
        self.conn = sqlite3.connect(f"{os.getcwd()}/{self._data_name}")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise exc_type


database_manager = MyDatabaseManager("students.db")


class DbSeeder:

    @staticmethod
    def post_marks(mark1, mark2, mark3):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO 'marks'('mark1', 'mark2', 'mark3') VALUES (?,?,?)",
                           [mark1, mark2, mark3])
            conn.commit()
            return 'OK'

    @staticmethod
    def post_student(name, surname, groups, curator_id, faculty_id):
        with database_manager as conn:
            cursor = conn.cursor()
            mark_id = cursor.execute("SELECT max(Id) FROM marks")
            mark_id = mark_id.fetchall()[0][0]
            cursor.execute(f"INSERT INTO 'student'('name', 'surname', 'groups', 'curator_id', 'faculty_id', 'mark_id') VALUES (?,?,?,?,?,?)",
                           [name, surname, groups, curator_id, faculty_id, mark_id])
            conn.commit()
            return 'OK'

