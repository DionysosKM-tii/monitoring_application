from dataclasses import dataclass

from backend.domain.entities.entity import Entity
from backend.domain.value_objects.geometry import Geometry


@dataclass
class AreaOfInterest(Entity):
    geometry: Geometry

    @classmethod
    def create_area(cls, geometry_dict: dict):
        geometry = Geometry.from_dict(geometry_dict)

        return cls(geometry=geometry)
