from dataclasses import dataclass
from http import HTTPStatus

from fastapi import APIRouter, Depends

from backend.application.use_cases.photo_use_cases import PhotoUseCases
from backend.interfaces.controllers.requests.add_photo_request import AddPhotoRequest
from backend.interfaces.controllers.views.photo_views import GetPhotoView

@dataclass
class PhotosController:
    photo_use_cases: PhotoUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/photos", tags=["photos"])

        self.router.post("/add", status_code=HTTPStatus.ACCEPTED)(self.add_photo_to_area)
        self.router.get("/{area_id}")(self.get_photos_by_area)

    async def add_photo_to_area(self, request: AddPhotoRequest = Depends()):
        photo_data = await request.photo.read()
        self.photo_use_cases.add_photo(request.area_id, request.photo_date, photo_data)

    async def get_photos_by_area(self, area_id: int) -> list[GetPhotoView]:
        photo_dtos = self.photo_use_cases.get_photos_by_area(area_id)
        return [GetPhotoView.from_dto(dto) for dto in photo_dtos]


