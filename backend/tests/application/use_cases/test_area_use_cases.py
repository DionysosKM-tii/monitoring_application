from unittest.mock import Mock

from backend.application.dtos.area_dto import AreaDTO
from backend.application.use_cases.area_use_cases import AreaUseCases


def test_create_area():
    # Arrange
    area_data_service = Mock()
    use_cases = AreaUseCases(area_data_service=area_data_service)
    given_geometry = {"type": "Polygon", "coordinates": [[[0, 0], [1, 1], [2, 2], [0, 0]]]}
    given_name = "Test Area"
    # Act
    use_cases.create_area(given_geometry, given_name)
    # Assert
    assert area_data_service.save_area.called
    args, kwargs = area_data_service.save_area.call_args
    assert isinstance(args[0], AreaDTO)
    assert args[1] == given_name


def test_get_all_areas():
    # Arrange
    area_data_service = Mock()
    expected_areas = [AreaDTO.from_model(1, None, "Area1")]
    area_data_service.get_all_areas.return_value = expected_areas
    use_cases = AreaUseCases(area_data_service=area_data_service)
    # Act
    result = use_cases.get_all_areas()
    # Assert
    assert result == expected_areas
    area_data_service.get_all_areas.assert_called_once()
