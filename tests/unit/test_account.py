import pytest
from werkzeug.exceptions import NotFound

from app import db
from app.models import Account


# Pushing the app to context for the whole package
@pytest.fixture()
def create_an_account(username="john", email="john@example.com"):
    account = Account(username=username, email=email)
    db.session.add(account)
    db.session.commit()
    yield account
    db.session.delete(account)
    db.session.commit()


def test_password_hashing():
    u = Account(username="susan", email="susan@example.com")
    u.set_password("cat")
    assert u.check_password("dog") is False
    assert u.check_password("cat") is True


def test_create_user():
    account = Account(username="john", email="john@example.com")
    db.session.add(account)
    db.session.commit()
    account_retrieved = db.get_or_404(Account, account.id)
    assert account == account_retrieved
    db.session.delete(account)
    db.session.commit()
    with pytest.raises(NotFound):
        db.get_or_404(Account, account.id)


# def test_create_account():
#     u = Account(username='susan', email='susan@example.com')
#     u.set_password('cat')
#     assert u.check_password('dog') is False
#     assert u.check_password('cat') is True
# GIVEN a User model
# WHEN a new User is created
# THEN check the email, hashed_password, and role fields are defined correctly
