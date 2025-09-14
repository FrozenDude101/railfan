import json
from sqlalchemy import Engine
from sqlmodel import Session

from api.db.models import Station, StationNode, Leg, LegPartialWay, LegWay, StockClass, Stock, Operator, Route, RouteLeg, RouteStation
from api.testData import TestData


def loadTestData(engine: Engine) -> None:
    with open("src/api/testData/testData.json") as testDataFile:
        data = json.load(testDataFile)
        del data["$schema"]
        testData = TestData(**data)

    with Session(engine) as session:
        stations: dict[int, Station] = {}
        legs: dict[int, Leg] = {}
        stockClasses: dict[int, StockClass] = {}

        for stationData in testData.stations:
            stations[stationData.ref] = Station(name = stationData.name)
            session.add(stations[stationData.ref])

            for nodeData in stationData.nodes:
                session.add(StationNode(osmNodeId = nodeData.osmNodeId, stationId = stations[stationData.ref].id))

        for legData in testData.legs:
            legs[legData.ref] = Leg(name = legData.name)
            session.add(legs[legData.ref])

            for wayData in legData.ways:
                session.add(LegWay(osmWayId = wayData.osmWayId, legId = legs[legData.ref].id))

            for partialWayData in legData.partialWays:
                session.add(LegPartialWay(
                    osmWayId = partialWayData.osmWayId,
                    fromNodeId = partialWayData.fromNodeId,
                    toNodeId = partialWayData.toNodeId,
                    legId = legs[legData.ref].id))

        for stockClassData in testData.stockClasses:
            stockClasses[stockClassData.ref] = StockClass(name = stockClassData.name)
            session.add(stockClasses[stockClassData.ref])

        for operatorData in testData.operators:
            operator = Operator(name = operatorData.name)
            session.add(operator)

            for stockData in operatorData.stock:
                session.add(Stock(unitNumber = stockData.unitNumber, stockClassId = stockClasses[stockData.stockClassRef].id, operatorId = operator.id))

            for routeData in operatorData.routes:
                route = Route(name = routeData.name, operatorId = operator.id)
                session.add(route)

                for index, routeStationRef in enumerate(routeData.stationRefs):
                    session.add(RouteStation(index = index, routeId = route.id, stationId = stations[routeStationRef].id))

                for index, routeLegRef in enumerate(routeData.legRefs):
                    session.add(RouteLeg(index = index, routeId = route.id, legId = legs[routeLegRef].id))
                
        session.commit()
