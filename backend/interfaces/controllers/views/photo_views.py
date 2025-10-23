from pydantic import BaseModel
from datetime import date
from backend.application.dtos.photo_dto import PhotoDTO

class GetPhotoView(BaseModel):
    id: int
    area_id: int
    photo_full_path: str
    photo_date: date
    
    @staticmethod
    def from_dto(photo_dto: PhotoDTO):
        return GetPhotoView(
            id=photo_dto.photo_id,
            area_id=photo_dto.area_id,
            photo_full_path=photo_dto.photo_full_path,
            photo_date=photo_dto.photo_date
        )