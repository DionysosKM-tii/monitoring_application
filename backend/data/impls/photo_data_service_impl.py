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
