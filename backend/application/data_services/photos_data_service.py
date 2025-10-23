from abc import ABC, abstractmethod

from backend.application.dtos.photo_dto import PhotoDTO


class PhotosDataService(ABC):

    @abstractmethod
    def save_photo(self, photo_dto: PhotoDTO) -> None:
        pass

    @abstractmethod
    def get_photos_by_area(self, area_id: int) -> list[PhotoDTO]:
        pass