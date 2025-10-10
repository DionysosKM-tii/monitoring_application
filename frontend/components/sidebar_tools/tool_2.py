from nicegui import ui


def create_tool_2():
    """Create Tool n.2 UI component."""
    with ui.expansion('Tool n.2', icon='layers'):
        ui.switch('Random switch (placeholder)', value=False)
        ui.checkbox('Random checkbox (placeholder)', value=True)
