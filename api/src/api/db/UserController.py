from typing import Sequence

from sqlmodel import select
from sqlalchemy.orm import Session

from api.db import Controller
from api.db.models import DbUser, UserRef

class UserController(Controller):
    
    def insertUser(self, user: DbUser) -> DbUser:
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
        return user
    
    def getUser(self, userId: int) -> DbUser | None:
        statement = select(DbUser).where(DbUser.userId == userId)
        with Session(self.engine) as session:
            return session.scalar(statement)
    
    def getUsers(self) -> Sequence[DbUser]:
        statement = select(DbUser)
        with Session(self.engine) as session:
            return session.scalars(statement).fetchall()

    def deleteUser(self, userId: int) -> None:
        with Session(self.engine) as session:
            session.delete(UserRef(userId=userId))
            session.commit()
        