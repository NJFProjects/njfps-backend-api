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


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.errors import bp as errors_bp  # noqa: E402, F401, I001

    app.register_blueprint(errors_bp)
    from app.auth import bp as auth_bp  # noqa: E402, F401, I001

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


from app import models  # noqa: E402, F401
