from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from config import Config


# Define ModelBase to specify a custom constraint naming convention.
# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/models/
class Base(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app, model_class=Base)
migrate = Migrate(app, db)
