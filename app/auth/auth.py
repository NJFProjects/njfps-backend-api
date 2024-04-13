import sqlalchemy as sa
from flask_httpauth import HTTPBasicAuth

from app import db
from app.errors import error_response
from app.models import Account

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = db.session.scalar(sa.select(Account).where(Account.username == username))
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)
