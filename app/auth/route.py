import sqlalchemy as sa
from flask import request

from app import db
from app.auth import bp
from app.errors.errors import bad_request
from app.models import Account


@bp.route("/accounts/<int:id>")
def get_accounts(id):
    # return "Hello World!"
    return db.get_or_404(Account, id).to_dict()


@bp.route("/register")
def register():
    data = request.get_json()
    if "username" not in data or "email" not in data or "password" not in data:
        return bad_request("must include username, email and password fields")
    if db.session.scalar(
        sa.select(Account).where(Account.username == data["username"])
    ):
        return bad_request("please use a different username")
    if db.session.scalar(sa.select(Account).where(Account.email == data["email"])):
        return bad_request("please use a different email address")
    account = Account()
    account.from_dict(data, new_user=True)
    db.session.add(account)
    db.session.commit()
    return account.to_dict(), 201


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
