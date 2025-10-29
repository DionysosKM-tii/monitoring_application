from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.application.data_services.measurements_data_service import MeasurementsDataService
from backend.application.dtos.measurement_dto import MeasurementDTO
from backend.data.models.measurements_model import MeasurementsModel


class MeasurementsDataServiceImpl(MeasurementsDataService):
    def __init__(self, session: Session):
        self.session = session

    def save_measurement(self, measurements_dto: MeasurementDTO) -> None:
        measurements_model = MeasurementsModel(
            id=measurements_dto.measurement_id,
            area_id=measurements_dto.area_id,
            timestamp=measurements_dto.timestamp,
            type=measurements_dto.metric_type,
            value=measurements_dto.metric_value
        )
        self.session.add(measurements_model)
        self.session.commit()
        self.session.refresh(measurements_model)

    def get_measurements_for_area_id(self, area_id: int) -> list[MeasurementDTO]:
        query = select(MeasurementsModel).filter(
            MeasurementsModel.area_id == area_id
        )
        measurements_models = self.session.scalars(query).all()

        return [
            MeasurementDTO(
                measurement_id=model.id,
                area_id=model.area_id,
                timestamp=model.timestamp,
                metric_type=model.type,
                metric_value=model.value
            ) for model in measurements_models
        ]

    def get_measurements_for_area_id_and_metric_type(self, area_id: int, metric_type: str) -> list[MeasurementDTO]:
        query = select(MeasurementsModel).filter(
            MeasurementsModel.area_id == area_id,
            MeasurementsModel.type == metric_type
        )
        measurements_models = self.session.scalars(query).all()

        return [
            MeasurementDTO(
                measurement_id=model.id,
                area_id=model.area_id,
                timestamp=model.timestamp,
                metric_type=model.type,
                metric_value=model.value
            ) for model in measurements_models
        ]