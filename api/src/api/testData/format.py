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
        self.nodes = [StationNodeTestData(osmNodeId = node) for node in nodes]

@dataclass
class LegWayTestData:
    osmWayId: int

@dataclass
class LegPartialWayTestData:
    osmWayId: int
    fromNodeId: int
    toNodeId: int

class LegTestData:
    ways: list[LegWayTestData]
    partialWays: list[LegPartialWayTestData]

    def __init__(self, ways: list[int] = [], partialWays: Json = []) -> None:
        self.ways = [LegWayTestData(osmWayId = way) for way in ways]
        self.partialWays = [LegPartialWayTestData(**partialWay) for partialWay in partialWays]

class TestData:
    stations: list[StationTestData]
    legs: list[LegTestData]

    def __init__(self, stations: Json, legs: Json) -> None:
        self.stations = [StationTestData(**station) for station in stations]
        self.legs = [LegTestData(**leg) for leg in legs]
