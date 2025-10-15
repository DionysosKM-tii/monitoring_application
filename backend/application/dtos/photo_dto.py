from dataclasses import dataclass
from datetime import date

from backend.domain.entities.photo import Photo


@dataclass(frozen=True)
class PhotoDTO:
    photo_id: int
    area_id: int
    photo_full_path: str
    photo_date: date

    @staticmethod
    def from_domain(photo: Photo, photo_dir: str):
        return PhotoDTO(
            photo_id=photo.id,
            area_id=photo.area_id,
            photo_full_path=f"{photo_dir}{photo.photo_name}",
            photo_date=photo.photo_date
        )