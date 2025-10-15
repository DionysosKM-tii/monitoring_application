from dataclasses import dataclass
from http import HTTPStatus

from fastapi import APIRouter, Depends

from backend.application.use_cases.photo_use_cases import PhotoUseCases
from backend.interfaces.controllers.requests.add_photo_request import AddPhotoRequest


@dataclass
class PhotosController:
    photo_use_cases: PhotoUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/photos", tags=["photos"])

        self.router.post("/add", status_code=HTTPStatus.ACCEPTED)(self.add_photo_to_area)

    async def add_photo_to_area(self, request: AddPhotoRequest = Depends()):
        photo_data = await request.photo.read()
        self.photo_use_cases.add_photo(request.area_id, request.photo_date, photo_data)

