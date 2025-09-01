from sqlmodel import SQLModel
from sqlalchemy import Engine

class Controller:
    engine: Engine

    def __init__(self, engine: Engine) -> None:
        SQLModel.metadata.create_all(engine)
        self.engine = engine
