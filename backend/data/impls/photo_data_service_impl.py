from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.application.data_services.photos_data_service import PhotosDataService
from backend.application.dtos.photo_dto import PhotoDTO
from backend.data.models.uploaded_photo_model import UploadedPhotoModel


class PhotoDataServiceImpl(PhotosDataService):
    def __init__(self, session: Session):
        self.session = session

    def save_photo(self, photo_dto: PhotoDTO) -> None:
        photo_model = UploadedPhotoModel(
            id=photo_dto.photo_id,
            area_id=photo_dto.area_id,
            photo_full_path=photo_dto.photo_full_path,
            photo_date=photo_dto.photo_date
        )
        self.session.add(photo_model)
        self.session.commit()
        self.session.refresh(photo_model)

    def get_photos_by_area(self, area_id: int) -> list[PhotoDTO]:
        query = select(UploadedPhotoModel).filter(
            UploadedPhotoModel.area_id == area_id
        )
        photo_models = self.session.scalars(query).all()
        
        return [
            PhotoDTO(
                photo_id=model.id,
                area_id=model.area_id,
                photo_full_path=model.photo_full_path,
                photo_date=model.photo_date
            )
            for model in photo_models
        ]