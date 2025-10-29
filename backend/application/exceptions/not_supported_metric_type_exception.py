from http import HTTPStatus

from backend.application.exceptions.application_exception import ApplicationException


class NotSupportedMetricTypeException(ApplicationException):

    def __init__(self, message: str, error_code: str):
        self.message = message
        self.error_code = error_code
        self.http_status_code = HTTPStatus.BAD_REQUEST
