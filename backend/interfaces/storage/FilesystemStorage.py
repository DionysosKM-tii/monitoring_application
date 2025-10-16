from backend.application.service_ports.storage_port import StoragePort


class FilesystemStorage(StoragePort):

    def store_photo(self, photo_name: str, photo_data: bytes) -> str:
        photos_dir = "photos/"
        photo_full_path = photos_dir + photo_name

        with open(photo_full_path, "wb") as photo_file:
            photo_file.write(photo_data)

        return photo_full_path