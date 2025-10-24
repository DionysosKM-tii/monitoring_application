from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends

from backend.application.dtos.measurement_dto import MeasurementDTO
from backend.application.use_cases.measurements_use_cases import MeasurementsUseCases
from backend.interfaces.controllers.requests.import_measurements_request import ImportMeasurementsRequest


@dataclass
class MeasurementsController:
    measurement_use_cases: MeasurementsUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/measurements", tags=["measurements"])

        self.router.post("/import-measurements/{area_id}", status_code=HTTPStatus.ACCEPTED)(self.import_measurements)

    async def import_measurements(self, area_id: int, request: ImportMeasurementsRequest = Depends()):
        # csv_data = await request.measurements.read()
        csv_rows = request.measurements.file.read().decode("utf-8").split("\n")[1:]
        measurements_dtos = [self._from_csv_row_to_measurement_dto(area_id, row) for row in csv_rows]

        self.measurement_use_cases.import_measurements_from_csv(measurements_dtos)

    @staticmethod
    def _from_csv_row_to_measurement_dto(area_id: int, csv_row: str) -> MeasurementDTO:
        if not csv_row.strip():
            # TODO: raise exception
            raise Exception("Empty CSV row")
        columns = [col.strip() for col in csv_row.split(",")]
        if len(columns) != 3:
            # TODO: raise exception
            raise Exception("Invalid CSV row")
        try:
            timestamp = datetime.strptime(columns[0], "%m/%d/%Y")
            metric_type = columns[1]
            metric_value = float(columns[2])
        except Exception as e:
            # TODO: raise exception
            raise Exception("Invalid CSV row")

        return MeasurementDTO(
            measurement_id=None,
            area_id=area_id,
            timestamp=timestamp,
            metric_type=metric_type,
            metric_value=metric_value
        )
