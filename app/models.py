from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class Account(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    projects: so.WriteOnlyMapped["Project"] = so.relationship(back_populates="author")

    def __repr__(self):
        return f"<Account {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def projects_count(self):
        query = sa.select(sa.func.count()).select_from(
            self.projects.select().subquery()
        )
        return db.session.scalar(query)

    def to_dict(self, include_email=False):
        data = {
            "id": self.id,
            "username": self.username,
            "project_count": self.projects_count(),
        }
        if include_email:
            data["email"] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ["username", "email"]:
            if field in data:
                setattr(self, field, data[field])
        if new_user and "password" in data:
            self.set_password(data["password"])


class Project(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc)
    )
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Account.id), index=True)

    author: so.Mapped[Account] = so.relationship(back_populates="projects")

    def __repr__(self):
        return f"<Project {self.body}>"
