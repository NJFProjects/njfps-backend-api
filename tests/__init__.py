import os

from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "test.db")
