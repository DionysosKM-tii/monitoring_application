from nicegui import ui
from frontend.components.sidebar_tools.tool_1 import create_tool_1
from frontend.components.sidebar_tools.tool_2 import create_tool_2

def create_sidebar():
    global DRAWER, AREA_TITLE

    DRAWER = ui.left_drawer(value=False).classes('bg-gray-100 w-80 p-3')
    with DRAWER:
        AREA_TITLE = ui.label('').classes('text-lg font-semibold')
        ui.separator()

        # Create individual tools
        create_tool_1()
        create_tool_2()
    
    return DRAWER


def sidebar_show(area: dict) -> None:
    if not DRAWER or not AREA_TITLE:
        return

    AREA_TITLE.set_text(area['area_name'])
    DRAWER.set_value(True)



def sidebar_hide() -> None:
    if not DRAWER:
        return

    DRAWER.set_value(False)

    if AREA_TITLE:
        AREA_TITLE.set_text('')