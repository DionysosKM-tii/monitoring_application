from dataclasses import dataclass
from typing import List

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass
class CreateAreaUseCase:
    area_data_service: AreaDataService

    def execute(self, geometry: dict, name: str) -> int:
        area = AreaOfInterest.create_area(geometry)
        area_id = self.area_data_service.save_area(AreaDTO.from_domain(area), name)

        return area_id


@dataclass
class GetAllAreasUseCase:
    area_data_service: AreaDataService

    def execute(self) -> List[AreaDTO]:
        # Get all areas as DTOs
        area_dtos = self.area_data_service.get_all_areas()

        # Convert DTOs to GetAreaView objects
        return self.area_data_service.get_all_areas()
