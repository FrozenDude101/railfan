from typing import Any
from dataclasses import dataclass


type Json = list[dict[str, Any]]


@dataclass
class StationNodeTestData:
    osmNodeId: int

class StationTestData:
    ref: int
    name: str
    nodes: list[StationNodeTestData]

    def __init__(self, ref: int, name: str, nodes: list[int]) -> None:
        self.ref = ref
        self.name = name
        self.nodes = [ StationNodeTestData(osmNodeId = node) for node in nodes ]

@dataclass
class LegWayTestData:
    osmWayId: int

@dataclass
class LegPartialWayTestData:
    osmWayId: int
    fromNodeId: int
    toNodeId: int

class LegTestData:
    ref: int
    name: str
    ways: list[LegWayTestData]
    partialWays: list[LegPartialWayTestData]

    def __init__(self, ref: int, name: str, ways: list[int] = [], partialWays: Json = []) -> None:
        self.ref = ref
        self.name = name
        self.ways = [ LegWayTestData(osmWayId = way) for way in ways ]
        self.partialWays = [ LegPartialWayTestData(**partialWay) for partialWay in partialWays ]

@dataclass
class StockClass:
    ref: int
    name: str

@dataclass
class Stock:
    ref: int
    unitNumber: int
    stockClassRef: int

@dataclass
class Route:
    ref: int
    name: str
    stationRefs: list[int]
    legRefs: list[int]

class Operator:
    name: str
    stock: list[Stock]
    routes: list[Route]

    def __init__(self, name: str, stock: Json, routes: Json) -> None:
        self.name = name
        self.stock = [ Stock(**stockItem) for stockItem in stock ]
        self.routes = [ Route(**route) for route in routes ]

@dataclass
class Journey:
    stockRef: int
    routeRef: int
    fromStationRef: int
    toStationRef: int

class User:
    displayName: str
    journeys: list[Journey]

    def __init__(self, displayName: str, journeys: Json) -> None:
        self.displayName = displayName
        self.journeys = [ Journey(**journey) for journey in journeys ]

class TestData:
    stations: list[StationTestData]
    legs: list[LegTestData]
    stockClasses: list[StockClass]
    operators: list[Operator]
    users: list[User]

    def __init__(self, stations: Json, legs: Json, stockClasses: Json, operators: Json, users: Json) -> None:
        self.stations = [ StationTestData(**station) for station in stations ]
        self.legs = [ LegTestData(**leg) for leg in legs ]
        self.stockClasses = [ StockClass(**stockClass) for stockClass in stockClasses ]
        self.operators = [ Operator(**operator) for operator in operators ]
        self.users = [ User(**user) for user in users ]
