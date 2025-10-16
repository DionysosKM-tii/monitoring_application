import os

from backend.application.exceptions.application_error_code import ApplicationErrorCode
from backend.application.exceptions.storage_exception import StorageException
from backend.application.service_ports.storage_port import StoragePort


class FilesystemStorage(StoragePort):

    def store_photo(self, photo_name: str, photo_data: bytes) -> str:
        photos_dir = "photos/"
        photo_full_path = photos_dir + photo_name

        try:
            with open(photo_full_path, "wb") as photo_file:
                photo_file.write(photo_data)
        except Exception as e:
            # In case of error, delete the file if it exists
            if os.path.exists(photo_full_path):
                os.remove(photo_full_path)
            raise StorageException(f"Failed to store photo: {photo_name}", ApplicationErrorCode.STORE_PHOTO_ERROR.name)

        return photo_full_path
