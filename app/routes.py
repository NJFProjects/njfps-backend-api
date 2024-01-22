from flask import request
from flask_restx import Api, Resource

from app import app

api = Api(app)

todos = {"todo1": "data=Remember the milk"}


@api.route("/<string:todo_id>")
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form["data"]
        return {todo_id: todos[todo_id]}


if __name__ == "__main__":
    app.run(debug=True)
