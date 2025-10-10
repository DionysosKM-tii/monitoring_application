from nicegui import ui


def create_tool_1():
    """Create Tool n.1 UI component."""
    with ui.expansion('Tool n.1', icon='edit'):
        ui.switch('Random switch (placeholder)', value=True)
        ui.checkbox('Random checkbox (placeholder)', value=False)
