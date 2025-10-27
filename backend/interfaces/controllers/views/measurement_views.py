from pydantic import BaseModel

from backend.application.dtos.measurement_dto import MeasurementDTO


class GetMeasurementView(BaseModel):
    area_id: int
    timestamp: str
    metric_type: str
    metric_value: float

    @staticmethod
    def from_dto(measurement_dto: MeasurementDTO):
        return GetMeasurementView(
            area_id=measurement_dto.area_id,
            timestamp=measurement_dto.timestamp.strftime("%Y-%m-%d"),
            metric_type=measurement_dto.metric_type,
            metric_value=measurement_dto.metric_value
        )