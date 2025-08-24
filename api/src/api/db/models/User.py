from __future__ import annotations

from sqlmodel import Field, SQLModel

class UserRef(SQLModel, table=False):
    userId: int = Field(primary_key=True)

class User(UserRef):
    displayName: str = Field(unique=True)

class AuthUser(User):
    email: str = Field(unique=True)

class DbUser(AuthUser, table=True):
    __tablename__ = "users"

    passwordHash: bytes