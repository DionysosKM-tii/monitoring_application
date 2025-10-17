from http import HTTPStatus


class ApplicationException(Exception):
    def __init__(self, message, error_code: str, http_status_code: HTTPStatus):
        self.message = message
        self.error_code = error_code
        self.http_status_code = http_status_code
