from abc import ABC, abstractmethod

from backend.domain.entities.area_of_interest import AreaOfInterest


class AreaRepository(ABC):
    @abstractmethod
    def save_area(self, area: AreaOfInterest) -> None:
        pass
