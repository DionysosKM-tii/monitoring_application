from dataclasses import dataclass

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.domain.entities.area_of_interest import AreaOfInterest


@dataclass
class CreateAreaUseCase:
    area_data_service: AreaDataService

    def execute(self, geometry: dict) -> int:
        area = AreaOfInterest(
            geometry
        )

        area_id = self.area_data_service.save_area(AreaDTO.from_domain(area))

        return area_id
