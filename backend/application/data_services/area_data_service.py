from abc import ABC, abstractmethod

from backend.application.dtos.area_dto import AreaDTO


class AreaDataService(ABC):

    @abstractmethod
    def save_area(self, area_dto: AreaDTO) -> int:
        pass
