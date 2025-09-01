from typing import Sequence

from sqlmodel import Session, select

from api.db import Controller
from api.db.models import Station

class StationController(Controller):
    
    def getStations(self) -> Sequence[Station]:
        statement = select(Station)
        with Session(self.engine) as session:
            return session.scalars(statement).fetchall()
        