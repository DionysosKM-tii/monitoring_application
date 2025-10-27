from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends

from backend.application.dtos.measurement_dto import MeasurementDTO
from backend.application.exceptions.application_error_code import ApplicationErrorCode
from backend.application.exceptions.invalid_import_exception import InvalidImportException
from backend.application.use_cases.measurements_use_cases import MeasurementsUseCases
from backend.interfaces.controllers.requests.import_measurements_request import ImportMeasurementsRequest
from backend.interfaces.controllers.views.measurement_views import GetMeasurementView


@dataclass
class MeasurementsController:
    measurement_use_cases: MeasurementsUseCases

    def __post_init__(self):
        self.router = APIRouter(prefix="/measurements", tags=["measurements"])

        self.router.post("/import-measurements/{area_id}", status_code=HTTPStatus.ACCEPTED)(self.import_measurements)
        self.router.get("/{area_id}", status_code=HTTPStatus.OK)(self.get_measurements_for_area_id)

    async def import_measurements(self, area_id: int, request: ImportMeasurementsRequest = Depends()):
        # csv_data = await request.measurements.read()
        csv_rows = request.measurements.file.read().decode("utf-8").split("\n")[1:]
        measurements_dtos = [self._from_csv_row_to_measurement_dto(area_id, row) for row in csv_rows]

        self.measurement_use_cases.import_measurements_from_csv(measurements_dtos)

    async def get_measurements_for_area_id(self, area_id: int) -> list[GetMeasurementView]:
        measurements_dtos = self.measurement_use_cases.get_measurements_for_area_id(area_id)

        return [
            GetMeasurementView.from_dto(
                dto
            ) for dto in measurements_dtos
        ]

    @staticmethod
    def _from_csv_row_to_measurement_dto(area_id: int, csv_row: str) -> MeasurementDTO:
        if not csv_row.strip():
            raise InvalidImportException("Empty csv row.", ApplicationErrorCode.IMPORT_MEASUREMENTS_ERROR.name)
        columns = [col.strip() for col in csv_row.split(",")]
        if len(columns) != 3:
            raise InvalidImportException(f"Wrong format for row: {csv_row}", ApplicationErrorCode.IMPORT_MEASUREMENTS_ERROR.name)
        try:
            timestamp = datetime.strptime(columns[0], "%m/%d/%Y")
            metric_type = columns[1]
            metric_value = float(columns[2])
        except Exception as e:
            raise InvalidImportException(f"Not able to parse row: {csv_row}", ApplicationErrorCode.IMPORT_MEASUREMENTS_ERROR.name)

        return MeasurementDTO(
            measurement_id=None,
            area_id=area_id,
            timestamp=timestamp,
            metric_type=metric_type,
            metric_value=metric_value
        )
