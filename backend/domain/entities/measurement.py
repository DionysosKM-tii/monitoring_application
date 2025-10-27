from dataclasses import dataclass
from datetime import date

from backend.application.exceptions.application_error_code import ApplicationErrorCode
from backend.application.exceptions.not_supported_metric_type_exception import NotSupportedMetricTypeException
from backend.domain.entities.entity import Entity
from backend.domain.value_objects.metric import Metric
from backend.domain.value_objects.metric_type import MetricType


@dataclass
class Measurement(Entity):
    area_id: int
    timestamp: date
    metric: Metric

    @classmethod
    def add_new_measurement(cls, area_id: int, timestamp: date, metric_type: str, metric_value: float):
        if metric_type not in MetricType:
            raise NotSupportedMetricTypeException(
                f"Metric type: {metric_type} is not supported", ApplicationErrorCode.NOT_SUPPORTED_METRIC_ERROR.name
            )
        metric = Metric(
            type=MetricType[metric_type],
            value=metric_value
        )

        return cls(
            area_id=area_id,
            timestamp=timestamp,
            metric=metric
        )
