from dataclasses import dataclass

from backend.application.data_services.measurements_data_service import MeasurementsDataService
from backend.application.dtos.measurement_dto import MeasurementDTO
from backend.domain.entities.measurement import Measurement


@dataclass
class MeasurementsUseCases:
    measurements_data_service: MeasurementsDataService

    def import_measurements_from_csv(self, measurements_dtos: list[MeasurementDTO]) -> None:
        for measurement_dto in measurements_dtos:
            measurement = Measurement.add_new_measurement(
                measurement_dto.area_id,
                measurement_dto.timestamp,
                measurement_dto.metric_type,
                measurement_dto.metric_value
            )
            # Normally here we should transform the entity object back to a DTO,
            #but since here we are not really changing the data, we can just use the dto
            self.measurements_data_service.save_measurement(measurement_dto)

