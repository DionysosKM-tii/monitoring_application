from fastapi import FastAPI, APIRouter

from backend.application.use_cases.area_use_cases import CreateAreaUseCase
from backend.data.configs.postgis_config import get_session
from backend.data.impls.area_data_service_impl import AreaDataServiceImpl
from backend.interfaces.controllers.areas_controller import AreasController

app = FastAPI()

router = APIRouter()
postgis_session = get_session()
create_area_use_case = CreateAreaUseCase(area_data_service=AreaDataServiceImpl(postgis_session))
areas_controller = AreasController(create_area_use_case)

app.include_router(areas_controller.router)
