from dataclasses import dataclass

from backend.domain.entities.entity import Entity
from backend.domain.value_objects.geometry import Geometry


@dataclass
class AreaOfInterest(Entity):
    geometry: Geometry
    name: str = ""
