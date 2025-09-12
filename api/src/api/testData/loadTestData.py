import json
from sqlalchemy import Engine
from sqlmodel import Session

from api.db.models import Station, StationNode, Leg, LegPartialWay, LegWay
from api.testData import TestData


def loadTestData(engine: Engine) -> None:
    with open("src/api/testData/testData.json") as testDataFile:
        data = json.load(testDataFile)
        del data["$schema"]
        testData = TestData(**data)

    with Session(engine) as session:
        for stationData in testData.stations:
            station = Station(name = stationData.name)
            session.add(station)

            for nodeData in stationData.nodes:
                session.add(StationNode(osmNodeId = nodeData.osmNodeId, stationId = station.id))

        session.commit()

        for legData in testData.legs:
            leg = Leg()
            session.add(leg)

            for wayData in legData.ways:
                session.add(LegWay(osmWayId = wayData.osmWayId, legId = leg.id))

            for partialWayData in legData.partialWays:
                session.add(LegPartialWay(
                    osmWayId = partialWayData.osmWayId,
                    fromNodeId = partialWayData.fromNodeId,
                    toNodeId = partialWayData.toNodeId,
                    legId = leg.id))
                
        session.commit()
