from flask import Flask
from flask_restful import Api
from sample6.app.resources import UserResource


app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/user')

if __name__ == "__main__":
    app.run(debug=True)
