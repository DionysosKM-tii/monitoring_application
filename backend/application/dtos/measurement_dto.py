from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class MeasurementDTO:
    measurement_id: Optional[int]
    area_id: int
    timestamp: date
    metric_type: str
    metric_value: float
