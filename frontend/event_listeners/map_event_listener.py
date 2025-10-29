from frontend.components.dtos.area_details_dto import AreaDetailsDTO
from frontend.components.sidebar import get_sidebar


def on_area_selected(area_details: AreaDetailsDTO) -> None:
    get_sidebar().show(area_details)


def on_area_deselected() -> None:
    get_sidebar().hide()
