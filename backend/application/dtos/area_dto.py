from dataclasses import dataclass


@dataclass(frozen=True)
class AreaDTO:
    id: int
    geometry: dict

    @staticmethod
    def from_domain(area_of_interest):
        return AreaDTO(
            area_of_interest.id,
            area_of_interest.geometry
        )
