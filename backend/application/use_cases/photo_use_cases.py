from dataclasses import dataclass
from datetime import date

from backend.application.data_services.photos_data_service import PhotosDataService
from backend.application.dtos.photo_dto import PhotoDTO
from backend.application.service_ports.storage_port import StoragePort
from backend.domain.entities.photo import Photo


@dataclass
class PhotoUseCases:
    photos_data_service: PhotosDataService
    storage_port: StoragePort

    def add_photo(self, area_id: int, photo_date: date, photo_data: bytes) -> None:
        photo_entity = Photo.add_new_photo(area_id, photo_date)

        photo_full_path = self.storage_port.store_photo(photo_entity.photo_name, photo_data)
        self.photos_data_service.save_photo(PhotoDTO.from_domain(photo_entity, photo_full_path))
