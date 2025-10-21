from nicegui import ui
from components.sidebar_tools.tool_1 import create_tool_1
from components.sidebar_tools.tool_2 import create_tool_2


def create_sidebar():
    """Create the collapsible sidebar with tools."""
    drawer = ui.left_drawer(value=False).classes('bg-gray-100 w-80 p-3')
    with drawer:
        ui.label('Tools').classes('text-lg font-semibold')
        ui.separator()
        
        # Create individual tools
        create_tool_1()
        create_tool_2()
    
    return drawer
