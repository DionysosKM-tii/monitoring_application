from fastapi import File, UploadFile


class ImportMeasurementsRequest:
    measurements: UploadFile

    def __init__(
            self,
            measurements: UploadFile = File(...)
    ):
        self.measurements = measurements