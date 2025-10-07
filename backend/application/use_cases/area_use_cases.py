from dataclasses import dataclass

from backend.application.dtos.area_dtos import CreateAreaDTO
from backend.application.repositories.area_repository import AreaRepository
from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass
class CreateAreaUseCase:
    area_repository: AreaRepository | None  # Replace 'any' with the actual type of your repository

    def execute(self, geometry: dict) -> str:
        area = AreaOfInterest(
            geometry
        )

        return str(area.id)