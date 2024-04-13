import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
rootdir = os.path.dirname(basedir)
load_dotenv(os.path.join(basedir, ".env"))


# Basic Config
class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "8061b54a249ef7e741c9be2b5232437bda972546712a55b3423af9d95446f41b"
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(rootdir, "app.db")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(rootdir, "test.db")
