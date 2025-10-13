from pydantic import BaseModel

from backend.application.dtos.area_dto import AreaDTO


class GetAreaView(BaseModel):
    id: int
    geometry: dict
    name: str

    @staticmethod
    def from_dto(area_dto: AreaDTO):
        return GetAreaView(
            id=area_dto.area_id,
            geometry=area_dto.geometry,
            name=area_dto.name
        )
