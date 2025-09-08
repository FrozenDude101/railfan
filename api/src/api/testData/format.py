from typing import Any

class OsmNode:
    id: int

    def __init__(self, id: int) -> None:
        self.id = id

class Station:
    name: str
    osmNodes: list[OsmNode]

    def __init__(self, name: str, osmNodes: list[int]) -> None:
        self.name = name
        self.osmNodes = [OsmNode(osmNode) for osmNode in osmNodes]

class TestData:
    stations: list[Station]

    def __init__(self, stations: list[dict[str, Any]]) -> None:
        self.stations = [Station(**station) for station in stations]
