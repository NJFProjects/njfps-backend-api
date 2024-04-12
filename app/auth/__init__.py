from flask import Blueprint

bp = Blueprint("auth", __name__)

from app.auth import route  # noqa: E402, F401
