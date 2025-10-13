from abc import ABC, abstractmethod
from typing import List

from backend.application.dtos.area_dto import AreaDTO


class AreaDataService(ABC):

    @abstractmethod
    def save_area(self, area_dto: AreaDTO, name: str) -> int:
        pass

    @abstractmethod
    def get_all_areas(self) -> List[AreaDTO]:
        pass
