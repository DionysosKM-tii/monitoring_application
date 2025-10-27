from abc import ABC, abstractmethod

from backend.application.dtos.measurement_dto import MeasurementDTO


class MeasurementsDataService(ABC):

    @abstractmethod
    def save_measurement(self, measurements_dto: MeasurementDTO) -> None:
        pass

    @abstractmethod
    def get_measurements_for_area_id(self, area_id: int) -> list[MeasurementDTO]:
        pass