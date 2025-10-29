from typing import Optional

from nicegui import ui, context

from frontend.components.dtos.area_details_dto import AreaDetailsDTO
from frontend.components.sidebar_tools.tool_1 import create_tool_1
from frontend.components.sidebar_tools.tool_2 import create_tool_2
from frontend.event_listeners.photos_event_listener import display_slideshow_for_area


class Sidebar:

    def __init__(self):
        self._drawer = ui.left_drawer(value=False).classes('bg-gray-100 w-80 p-3')
        self._current_area: Optional[AreaDetailsDTO] = None

    def show(self, area_details: AreaDetailsDTO):
        self._current_area = area_details

        self._drawer.clear()
        with self._drawer:
            ui.label(area_details.area_name).classes('text-lg font-semibold')
            ui.separator()
            create_tool_1()
            create_tool_2()
            ui.separator()
            ui.button('Show Slideshow', on_click=lambda: display_slideshow_for_area(area_details.area_id))
        self._drawer.set_value(True)

    def hide(self):
        self._drawer.set_value(False)
        self._current_area = None


def get_sidebar() -> Sidebar:
    client = context.client

    if not hasattr(client, '_sidebar_instance'):
        client._sidebar_instance = Sidebar()

    return client._sidebar_instance
