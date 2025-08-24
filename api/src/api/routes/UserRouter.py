from fastapi import APIRouter

from api.db import UserController
from api.db.models import User

class UserRouter():
    router: APIRouter
    userController: UserController

    def __init__(self, userController: UserController) -> None:
        self.userController = userController

        self.router = APIRouter(prefix = "/users")
        self.router.get("/")(self._root)

    def _root(self) -> list[User]:
        return list(self.userController.getUsers())
