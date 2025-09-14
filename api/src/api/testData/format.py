from typing import Any
from dataclasses import dataclass


type Json = list[dict[str, Any]]


@dataclass
class StationNodeTestData:
    osmNodeId: int

class StationTestData:
    name: str
    nodes: list[StationNodeTestData]

    def __init__(self, name: str, nodes: list[int]) -> None:
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
    name: str
    ways: list[LegWayTestData]
    partialWays: list[LegPartialWayTestData]

    def __init__(self, name: str, ways: list[int] = [], partialWays: Json = []) -> None:
        self.name = name
        self.ways = [ LegWayTestData(osmWayId = way) for way in ways ]
        self.partialWays = [ LegPartialWayTestData(**partialWay) for partialWay in partialWays ]

@dataclass
class StockClass:
    name: str

@dataclass
class Stock:
    unitNumber: int
    stockClass: str

class Operator:
    name: str
    stock: list[Stock]

    def __init__(self, name: str, stock: Json) -> None:
        self.name = name
        self.stock = [ Stock(**stockItem) for stockItem in stock ]

class TestData:
    stations: list[StationTestData]
    legs: list[LegTestData]
    stockClasses: list[StockClass]
    operators: list[Operator]

    def __init__(self, stations: Json, legs: Json, stockClasses: Json, operators: Json) -> None:
        self.stations = [ StationTestData(**station) for station in stations ]
        self.legs = [ LegTestData(**leg) for leg in legs ]
        self.stockClasses = [ StockClass(**stockClass) for stockClass in stockClasses ]
        self.operators = [ Operator(**operator) for operator in operators ]
