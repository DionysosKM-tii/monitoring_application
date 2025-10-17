from abc import ABC, abstractmethod

from backend.application.dtos.photo_dto import PhotoDTO


class PhotosDataService(ABC):

    @abstractmethod
    def save_photo(self, photo_dto: PhotoDTO) -> None:
        pass