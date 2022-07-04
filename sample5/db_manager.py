import sqlite3
from flask import jsonify
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


class DbCommands:

    @staticmethod
    def get_all():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT name,surname,groups,fname,sname,faculty FROM student INNER JOIN curator ON student.curator_id = curator.id INNER JOIN faculty ON student.faculty_id = faculty.Id")
            return jsonify(res.fetchall())

    @staticmethod
    def get_students():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT name,surname,groups FROM student ")
            return jsonify(res.fetchall())

    @staticmethod
    def get_marks():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT mark1,mark2,mark3 FROM marks ")
            return jsonify(res.fetchall())

    @staticmethod
    def get_curator():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT * FROM curator")
            return jsonify(res.fetchall())

    @staticmethod
    def get_faculty():
        with database_manager as conn:
            cursor = conn.cursor()
            res = cursor.execute("SELECT * FROM faculty")
            return jsonify(res.fetchall())

    @staticmethod
    def delete_student(Id):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE Id = ?", [Id])
            conn.commit()
            return "OK"

    @staticmethod
    def delete_marks(Id):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM marks WHERE Id = ?", [Id])
            conn.commit()
            return "OK"

    @staticmethod
    def delete_curator(Id):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM curator WHERE Id = ?", [Id])
            conn.commit()
            return "OK"

    @staticmethod
    def delete_faculty(Id):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM faculty WHERE Id = ?", [Id])
            conn.commit()
            return "OK"

    @staticmethod
    def put_student(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE student SET name = ?, surname = ? WHERE Id = ?",
                           [data['name'], data['surname'], data['Id']])
            conn.commit()
            return "OK"

    @staticmethod
    def put_marks(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE marks SET mark1 = ?, mark2 = ?, mark3 = ? WHERE Id = ?",
                           [data['mark1'], data['mark2'], data['mark3'], data['Id']])
            conn.commit()
            return "OK"

    @staticmethod
    def put_curator(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE curator SET fname = ?, sname = ? WHERE Id = ?",
                                   [data['fname'], data['sname'], data['Id']])
            conn.commit()
            return "OK"

    @staticmethod
    def put_faculty(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE faculty SET faculty = ? WHERE Id = ?",
                           [data['faculty'], data['Id']])
            conn.commit()
            return "OK"

    @staticmethod
    def post_student(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO 'student'('name', 'surname', 'groups','curator_id', 'faculty_id') VALUES (?,?,?,?,?)"
                , [data['name'], data['surname'], data['groups'], data['curator_id'], data['faculty_id']])
            conn.commit()
            return 'OK'

    @staticmethod
    def post_marks(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO 'marks'('mark1', 'mark2', 'mark3') VALUES (?,?,?)",
                           [data['mark1'], data['mark2'], data['mark3']])
            conn.commit()
            return 'OK'

    @staticmethod
    def post_curator(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO 'curator'('fname', 'sname') VALUES (?,?)"
                           , [data['fname'], data['sname']])
            conn.commit()
            return 'OK'

    @staticmethod
    def post_faculty(data):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO 'faculty'('faculty') VALUES (?)"
                , [data['faculty']])
            conn.commit()
            return 'OK'

    @staticmethod
    def show_students_by_curator(Id):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, surname FROM student WHERE curator_id = ?", [Id])
            return jsonify(cursor.fetchall())

    @staticmethod
    def show_top_students_by_faculty(faculty):
        with database_manager as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name, surname FROM student INNER JOIN faculty ON student.faculty_id = faculty.ID INNER JOIN marks ON student.mark_id = marks.ID WHERE (mark1+mark2+mark3)/3 > 4.5 and faculty = ?", [faculty])
            return jsonify(cursor.fetchall())