from dataclasses import dataclass

from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass(frozen=True)
class AreaDTO:
    id: int
    geometry: dict

    @staticmethod
    def from_domain(area_of_interest: AreaOfInterest):
        return AreaDTO(
            area_of_interest.id,
            area_of_interest.geometry
        )
