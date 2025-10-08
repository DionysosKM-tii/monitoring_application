from geoalchemy2.shape import from_shape
from sqlalchemy.orm import Session
from shapely.geometry import shape

from backend.application.data_services.area_data_service import AreaDataService
from backend.application.dtos.area_dto import AreaDTO
from backend.data.models.area_of_interest_model import AreaOfInterestModel


class AreaDataServiceImpl(AreaDataService):
    def __init__(self, session: Session):
        self.session = session

    def save_area(self, area_dto: AreaDTO) -> int:
        geom = from_shape(shape(area_dto.geometry))

        aoim = AreaOfInterestModel(
            id=area_dto.id,
            geometry=geom
        )
        self.session.add(aoim)
        self.session.commit()
        self.session.refresh(aoim)

        return aoim.id