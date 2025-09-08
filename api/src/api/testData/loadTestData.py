import json
from sqlalchemy import Engine
from sqlmodel import Session

from api.db.models import Station, OsmNode
from api.testData import TestData


def loadTestData(engine: Engine) -> None:
    with open("src/api/testData/testData.json") as testDataFile:
        testData = TestData(**json.load(testDataFile))

    with Session(engine) as session:
        for stationData in testData.stations:
            station = Station(name=stationData.name)
            session.add(station)
            for osmNodeData in stationData.osmNodes:
                osmNode = OsmNode(id=osmNodeData.id, stationId=station.id)
                session.add(osmNode)
        session.commit()
