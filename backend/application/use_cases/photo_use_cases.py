from dataclasses import dataclass
from datetime import date

from backend.application.data_services.photos_data_service import PhotosDataService
from backend.application.dtos.photo_dto import PhotoDTO
from backend.domain.entities.photo import Photo


@dataclass
class PhotoUseCases:
    photos_data_service: PhotosDataService

    def add_photo(self, area_id: int, photo_date: date, photo_data: bytes) -> None:
        photos_dir = "photos/"
        photo_entity = Photo.add_new_photo(area_id, photo_date)

        # TODO
        # first save the photo in the file system
        # then save the photo metadata in the database

        self.photos_data_service.save_photo(PhotoDTO.from_domain(photo_entity, photos_dir))
