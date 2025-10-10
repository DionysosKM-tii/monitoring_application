from dataclasses import dataclass

from fastapi import APIRouter

from backend.application.use_cases.area_use_cases import CreateAreaUseCase, GetAllAreasUseCase
from backend.interfaces.controllers.requests.area_requests import CreateAreaRequest


@dataclass
class AreasController:
    create_area_use_case: CreateAreaUseCase
    get_all_areas_use_case: GetAllAreasUseCase

    def __post_init__(self):
        self.router = APIRouter(prefix="/areas", tags=["areas"])

        self.router.post("/create")(self.create_area)
        self.router.get("/")(self.get_all_areas)

    async def create_area(self, request: CreateAreaRequest):
        area_id = self.create_area_use_case.execute(request.geometry)

        return {"area_id": area_id}

    async def get_all_areas(self):
        areas = self.get_all_areas_use_case.execute()

        return {"areas": areas}
