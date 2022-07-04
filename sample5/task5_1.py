
from flask import Flask, request
from sample5.db_manager import DbCommands

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show():
    if request.method == 'GET':
        return DbCommands.get_all()


@app.route('/name', methods=['GET', 'POST', 'PUT', 'DELETE'])
def names():
    if request.method == 'GET':
        return DbCommands.get_students()
    elif request.method == 'POST':
        return DbCommands.post_student(request.json)

    elif request.method == 'PUT':
        return DbCommands.put_student(request.json)
    else:
        return DbCommands.delete_student(request.json)


@app.route('/name/<int:curator_id>', methods=['GET'])
def get_student(curator_id=None):
    if curator_id:
        return DbCommands.show_students_by_curator(curator_id)


@app.route('/name/<string:faculty>', methods=['GET'])
def get_top_student(faculty=None):
    if faculty:
        return DbCommands.show_top_students_by_faculty(faculty)


@app.route('/mark', methods=['GET', 'POST', 'PUT', 'DELETE'])
def marks():
    if request.method == 'GET':
        return DbCommands.get_marks()
    elif request.method == 'POST':
        return DbCommands.post_marks(request.json)

    elif request.method == 'PUT':
        return DbCommands.put_marks(request.json)
    else:
        return DbCommands.delete_marks(request.json)


@app.route('/curator', methods=['GET', 'POST', 'PUT', 'DELETE'])
def curator():
    if request.method == 'GET':
        return DbCommands.get_curator()
    elif request.method == 'POST':
        return DbCommands.post_curator(request.json)

    elif request.method == 'PUT':
        return DbCommands.put_curator(request.json)
    else:
        return DbCommands.delete_curator(request.json)


@app.route('/faculty', methods=['GET', 'POST', 'PUT', 'DELETE'])
def faculty():
    if request.method == 'GET':
        return DbCommands.get_faculty()
    elif request.method == 'POST':
        return DbCommands.post_faculty(request.json)

    elif request.method == 'PUT':
        return DbCommands.put_faculty(request.json)
    else:
        return DbCommands.delete_faculty(request.json)


app.run(debug=True)
