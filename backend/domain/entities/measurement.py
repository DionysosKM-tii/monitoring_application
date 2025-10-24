from dataclasses import dataclass
from datetime import date

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
        if metric_type not in MetricType._member_names_:
            # TODO: raise exception
            raise Exception("Invalid metric type")
        metric = Metric(
            type=metric_type,
            value=metric_value
        )

        return cls(
            area_id=area_id,
            timestamp=timestamp,
            metric=metric
        )