from abc import ABC, abstractmethod

class StoragePort(ABC):

    @abstractmethod
    def store_photo(self, photo_name: str, photo_data: bytes) -> str:
        """Store a photo and return its URL or identifier."""
        pass