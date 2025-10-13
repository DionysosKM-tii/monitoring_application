from dataclasses import dataclass

from fastapi import APIRouter

from backend.application.use_cases.area_use_cases import AreaUseCases
from backend.interfaces.controllers.requests.area_requests import CreateAreaRequest
from backend.interfaces.controllers.views.area_views import GetAreaView


@dataclass
class AreasController:
    area_use_cases: AreaUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/areas", tags=["areas"])

        self.router.post("/create")(self.create_area)
        self.router.get("")(self.get_all_areas)

    async def create_area(self, request: CreateAreaRequest):
        area_id = self.area_use_cases.create_area(request.geometry, request.name)

        return {"area_id": area_id}

    async def get_all_areas(self):
        area_dtos = self.area_use_cases.get_all_areas()
        area_views = [
            GetAreaView.from_dto(
                dto
            ) for dto in area_dtos
        ]

        return {"areas": area_views}
