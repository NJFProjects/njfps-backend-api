from flask_restx import Api, Resource

from app import app, db
from app.models import Account

api = Api(app)

# todos = {"todo1": "data=Remember the milk"}


# @api.route("/<string:todo_id>")
# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form["data"]
#         return {todo_id: todos[todo_id]}


@api.route("/accounts/<int:id>")
class AccountApi(Resource):
    def get(self, id):
        return db.get_or_404(Account, id).to_dict()


# @api.route('/users', methods=['GET'])
# def get_users():
#     pass

# @api.route('/users', methods=['POST'])
# def create_user():
#     pass

# @api.route('/users/<int:id>', methods=['PUT'])
# def update_user(id):
#     pass

# if __name__ == "__main__":
#     app.run(debug=True)
