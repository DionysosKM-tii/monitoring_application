from dataclasses import dataclass
from http import HTTPStatus

from fastapi import APIRouter

from backend.application.use_cases.area_use_cases import AreaUseCases
from backend.interfaces.controllers.requests.area_requests import CreateAreaRequest
from backend.interfaces.controllers.views.area_views import GetAreaView


@dataclass
class AreasController:
    area_use_cases: AreaUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/areas", tags=["areas"])

        self.router.post("/create", status_code=HTTPStatus.CREATED)(self.create_area)
        self.router.get("")(self.get_all_areas)

    async def create_area(self, request: CreateAreaRequest) -> None:
        self.area_use_cases.create_area(request.geometry, request.name)

    async def get_all_areas(self) -> list[GetAreaView]:
        area_dtos = self.area_use_cases.get_all_areas()

        return [
            GetAreaView.from_dto(
                dto
            ) for dto in area_dtos
        ]
