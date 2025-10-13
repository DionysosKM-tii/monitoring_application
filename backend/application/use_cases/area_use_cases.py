from dataclasses import dataclass
from typing import List

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass
class AreaUseCases:
    area_data_service: AreaDataService

    def create_area(self, geometry: dict, name: str) -> int:
        area = AreaOfInterest.create_area(geometry)
        area_id = self.area_data_service.save_area(AreaDTO.from_domain(area), name)

        return area_id

    def get_all_areas(self) -> List[AreaDTO]:
        return self.area_data_service.get_all_areas()
