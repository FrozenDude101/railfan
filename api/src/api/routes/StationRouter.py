from fastapi import APIRouter

from api.db import StationController
from api.db.models import Station

class StationRouter():
    router: APIRouter
    stationController: StationController

    def __init__(self, stationController: StationController) -> None:
        self.stationController = stationController

        self.router = APIRouter(prefix = "/stations")
        self.router.get("/")(self._root)

    def _root(self) -> list[Station]:
        return list(self.stationController.getStations())
