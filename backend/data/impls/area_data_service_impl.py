from typing import List

from geoalchemy2.shape import from_shape
from shapely.geometry import shape
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.data.mappers import area_of_interest_model_mappers as area_mapper
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
        query = select(AreaOfInterestModel)
        areas = self.session.scalars(query).all()

        return [
            area_mapper.to_dto(
                area
            ) for area in areas
        ]
