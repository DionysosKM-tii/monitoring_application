from dataclasses import dataclass
from typing import List

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.domain.entities.area_of_interest import AreaOfInterest
from backend.interfaces.controllers.views.area_views import GetAreaView

@dataclass
class CreateAreaUseCase:
    area_data_service: AreaDataService

    def execute(self, geometry: dict) -> int:
        area = AreaOfInterest(
            geometry
        )

        area_id = self.area_data_service.save_area(AreaDTO.from_domain(area))

        return area_id


@dataclass
class GetAllAreasUseCase:
    area_data_service: AreaDataService

    def execute(self) -> List[GetAreaView]:
        # Get all areas as DTOs
        areas = self.area_data_service.get_all_areas()
        
        # Convert DTOs to GetAreaView objects
        return [
            GetAreaView(id=area.id, geometry=area.geometry)
            for area in areas
        ]
