from dataclasses import dataclass
from datetime import date
from uuid import uuid4

from backend.domain.entities.entity import Entity


@dataclass
class Photo(Entity):
    area_id: int
    photo_name: str
    photo_date: date

    @classmethod
    def add_new_photo(cls, area_id: int, photo_date: date):
        photo_name = f"{uuid4()}.png"

        return cls(
            area_id=area_id,
            photo_name=photo_name,
            photo_date=photo_date
        )
