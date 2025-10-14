from typing import Protocol


class Geometry(Protocol):
    geometry_type: str
    coordinates: list

    def __init__(self, geometry_type: str, coordinates: list):
        self.geometry_type = geometry_type
        self.coordinates = coordinates

    def to_dict(self) -> dict:
        return {
            "type": self.geometry_type,
            "coordinates": self.coordinates,
        }

    @classmethod
    def from_dict(cls, data: dict):
        data_type = data.get("type")
        if data_type is None:
            raise ValueError("Geometry type is required")

        data_coordinates = data.get("coordinates")
        if data_coordinates is None:
            raise ValueError("Geometry coordinates are required")

        return cls(
            geometry_type=data_type,
            coordinates=data_coordinates
        )
