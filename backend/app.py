from fastapi import FastAPI, APIRouter

from backend.application.use_cases.area_use_cases import AreaUseCases
from backend.application.use_cases.photo_use_cases import PhotoUseCases
from backend.data.configs.postgis_config import postgis_get_session
from backend.data.impls.area_data_service_impl import AreaDataServiceImpl
from backend.data.impls.photo_data_service_impl import PhotoDataServiceImpl
from backend.interfaces.controllers.areas_controller import AreasController
from backend.interfaces.controllers.photos_contoller import PhotosController

app = FastAPI()

router = APIRouter()
postgis_session = postgis_get_session()
# Data Services
area_data_service = AreaDataServiceImpl(postgis_session)
photo_data_service = PhotoDataServiceImpl(postgis_session)
# Use Cases
area_use_cases = AreaUseCases(area_data_service=area_data_service)
photo_use_cases = PhotoUseCases(photos_data_service=photo_data_service)
# Controllers
areas_controller = AreasController(area_use_cases)
photos_controller = PhotosController(photo_use_cases=photo_use_cases)

app.include_router(areas_controller.router)
app.include_router(photos_controller.router)