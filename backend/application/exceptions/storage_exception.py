from http import HTTPStatus

from backend.application.exceptions.base_esception import ApplicationException


class StorageException(ApplicationException):
    """Base class for storage-related exceptions."""

    def __init__(self, message: str, error_code: str):
        self.message = message
        self.error_code = error_code
        self.http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR
