from typing import List

from geoalchemy2.shape import from_shape
from geoalchemy2.shape import to_shape
from shapely.geometry import mapping
from shapely.geometry import shape
from sqlalchemy.orm import Session

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.data.models.area_of_interest_model import AreaOfInterestModel


class AreaDataServiceImpl(AreaDataService):
    def __init__(self, session: Session):
        self.session = session

    def save_area(self, area_dto: AreaDTO, name: str) -> None:
        geom = from_shape(shape(area_dto.geometry))
        aoim = AreaOfInterestModel(
            id=area_dto.area_id,
            geometry=geom,
            name=name
        )
        self.session.add(aoim)
        self.session.commit()
        self.session.refresh(aoim)

    def get_all_areas(self) -> List[AreaDTO]:
        areas = self.session.query(AreaOfInterestModel).all()

        return [
            AreaDTO.from_model(
                area.id,
                # Convert WKB to GeoJSON format
                mapping(to_shape(area.geometry)),
                area.name
            ) for area in areas
        ]
