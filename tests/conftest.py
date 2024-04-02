import pytest

from app import create_app, db
from app.models import Account
from config import TestConfig


# Pushing the app to context for the whole package
@pytest.fixture(autouse=True, scope="package")
def app_context_setup():
    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()
    yield
    db.session.remove()
    db.drop_all()
    app_context.pop()


# Pushing the app to context for the whole package
@pytest.fixture(scope="package")
def create_an_account(
    username="john", email="john@example.com", password="thisisalongpassword"
):
    account = Account(username=username, email=email)
    account.set_password(password)
    db.session.add(account)
    db.session.commit()
    yield account
    db.session.delete(account)
    db.session.commit()
