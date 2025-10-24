from dataclasses import dataclass

from backend.domain.value_objects.metric_type import MetricType


@dataclass
class Metric:
    type: MetricType
    value: float
