from dataclasses import dataclass

from backend.domain.value_objects.geometry import Geometry


@dataclass(frozen=True)
class CreateAreaDTO:
    geometry: Geometry
