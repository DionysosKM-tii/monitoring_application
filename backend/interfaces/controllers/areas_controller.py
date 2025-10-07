from fastapi import APIRouter

from backend.application.use_cases.area_use_cases import CreateAreaUseCase
from backend.interfaces.controllers.requests.area_requests import CreateAreaRequest

router = APIRouter()


@router.post("/create")
def create_area(request: CreateAreaRequest):
    area_id = CreateAreaUseCase.execute(request.geometry)

    return {"area_id": area_id}
