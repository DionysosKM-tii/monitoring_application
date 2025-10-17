from dataclasses import dataclass

from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass(frozen=True)
class AreaDTO:
    area_id: int
    geometry: dict
    name: str = None

    @staticmethod
    def from_domain(area_of_interest: AreaOfInterest) -> "AreaDTO":
        return AreaDTO(
            area_of_interest.id,
            area_of_interest.geometry.to_dict(),
        )
