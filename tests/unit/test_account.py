import pytest
from werkzeug.exceptions import NotFound

from app import db
from app.models import Account


# GIVEN a User model
# WHEN a new User is created
# THEN check if the new User could be retrieved successfully
def test_create_account():
    account = Account(username="john", email="john@example.com")
    db.session.add(account)
    db.session.commit()
    account_retrieved = db.get_or_404(Account, account.id)
    assert account == account_retrieved
    db.session.delete(account)
    db.session.commit()
    with pytest.raises(NotFound):
        db.get_or_404(Account, account.id)


# GIVEN a User model
# WHEN the User set the password
# THEN check if the password are hashed and could identified the new entry of password
def test_password_hashing():
    u = Account(username="susan", email="susan@example.com")
    u.set_password("cat")
    assert u.check_password("dog") is False
    assert u.check_password("cat") is True
