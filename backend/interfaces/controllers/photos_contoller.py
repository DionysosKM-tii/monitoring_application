from dataclasses import dataclass

from fastapi import APIRouter, Depends

from backend.interfaces.controllers.requests.add_photo_request import AddPhotoRequest


@dataclass
class PhotosController:

    def __post_init__(self):
        self.router = APIRouter(prefix="/photos", tags=["photos"])

        self.router.post("/add")(self.add_photo_to_area)

    async def add_photo_to_area(self, request: AddPhotoRequest = Depends()):
        return {"message": "Photo added to area"}
