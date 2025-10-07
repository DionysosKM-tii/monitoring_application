from fastapi import FastAPI, APIRouter

from backend.application.use_cases.area_use_cases import CreateAreaUseCase
from backend.interfaces.controllers.areas_controller import AreasController

# from backend.interfaces.controllers.areas_controller import router as areas

app = FastAPI()

router = APIRouter()
create_area_use_case = CreateAreaUseCase(area_repository=None)
areas_controller = AreasController(create_area_use_case)

app.include_router(areas_controller.router)
