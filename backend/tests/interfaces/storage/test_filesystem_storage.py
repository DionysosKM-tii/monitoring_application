import builtins
from http import HTTPStatus

import pytest

from backend.application.exceptions.application_error_code import ApplicationErrorCode
from backend.application.exceptions.storage_exception import StorageException
from backend.interfaces.storage.filesystem_storage import FilesystemStorage


def test_store_photo_happy_flow(monkeypatch):
    # Arrange
    storage = FilesystemStorage()
    given_photo_name = "test_photo.png"
    given_photo_data = b"test_photo_data"
    expected_photo_full_path = "photos/test_photo.png"

    written = {}

    class DummyFile:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def write(self, data: bytes):
            written["data"] = data
            return len(data)

    def mock_open(file, mode="r", *args, **kwargs):
        # capture the path used by FilesystemStorage
        written["path"] = file
        # Ensure binary write mode is used as expected
        assert "b" in mode
        return DummyFile()

    monkeypatch.setattr(builtins, "open", mock_open)

    # Act
    actual_photo_full_path = storage.store_photo(given_photo_name, given_photo_data)

    # Assert
    assert actual_photo_full_path == expected_photo_full_path
    assert written["path"] == expected_photo_full_path
    assert written["data"] == given_photo_data


def test_store_photo_error_path_raises_storage_exception(monkeypatch):
    # Arrange
    storage = FilesystemStorage()
    given_photo_name = "test_photo.png"
    given_photo_data = b"irrelevant"
    expected_photo_full_path = "photos/test_photo.png"

    called = {}

    def mock_open(file, mode="r", *args, **kwargs):
        # capture what the implementation attempts to open
        called["file"] = file
        called["mode"] = mode
        # simulate a filesystem failure inside the try block
        raise OSError("simulated write failure")

    monkeypatch.setattr(builtins, "open", mock_open)

    # Act
    with pytest.raises(StorageException) as exc_info:
        storage.store_photo(given_photo_name, given_photo_data)

    err = exc_info.value

    # Assert
    assert isinstance(err, StorageException)
    assert err.message == f"Failed to store photo: {given_photo_name}"
    assert err.error_code == ApplicationErrorCode.STORE_PHOTO_ERROR.name
    assert err.http_status_code == HTTPStatus.INTERNAL_SERVER_ERROR
