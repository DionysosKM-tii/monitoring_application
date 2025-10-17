from geoalchemy2.shape import to_shape
from shapely.geometry import mapping

from backend.application.dtos.area_dto import AreaDTO
from backend.data.models import AreaOfInterestModel


def to_dto(area_of_interest_model: AreaOfInterestModel) -> AreaDTO:
    return AreaDTO(
        area_of_interest_model.id,
        mapping(to_shape(area_of_interest_model.geometry)),
        area_of_interest_model.name
    )
