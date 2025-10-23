from nicegui import ui
from components.sidebar_tools.tool_1 import create_tool_1
from components.sidebar_tools.tool_2 import create_tool_2


def create_sidebar():
    """Create the collapsible sidebar with tools."""
    drawer = ui.left_drawer(value=False).classes('bg-gray-100 w-80 p-3')
    with drawer:
        area_header = ui.label().classes('text-lg font-semibold')
        ui.separator()
        ui.label('Tools').classes('text-lg font-semibold mt-2')
        # Create individual tools
        create_tool_1()
        create_tool_2()
    drawer.area_header = area_header
    return drawer

def update_drawer_content(drawer, area):
    """Update ONLY the info panel; tools remain intact."""
    drawer.area_header.text = f"{area['name']} (ID: {area['id']})"
