from nicegui import ui
from frontend.clients.api_client import api_client

class AreaNameDialog:
    """Dialog for collecting area name from user."""
    
    def __init__(self, geometry: dict):
        self.geometry = geometry
        self.dialog = None
        self.name_input = None
    
    def handle_confirm(self):
        """Handle confirm button click."""
        name = self.name_input.value.strip()
        self.dialog.close()
        
        # Execute API call directly
        ui.notify(f'Saving area "{name}"...', type='info')
        try:
            api_client.post_area(self.geometry, name)
            ui.notify(f'Area "{name}" saved successfully!', type='positive')
        except Exception as ex:
            ui.notify(f'Failed to save area: {str(ex)}', type='negative')
    
    def handle_cancel(self):
        """Handle cancel button click."""
        self.dialog.close()
        ui.notify('Area creation cancelled', type='info')
        # Redirect to homepage
        ui.navigate.to('/')
    
    def show(self):
        """Display the dialog."""
        with ui.dialog() as self.dialog, ui.card():
            ui.label('Enter Area Name').classes('text-h6 mb-4')
            self.name_input = ui.input(
                placeholder='Area name...',
                validation={'Required': lambda value: bool(value.strip())}
            ).classes('w-full')
            
            with ui.row().classes('w-full justify-end gap-2 mt-4'):
                ui.button('Cancel', on_click=self.handle_cancel).props('flat')
                ui.button('Confirm', on_click=self.handle_confirm).props('color=primary')
        
        self.dialog.open()
        self.name_input.run_method('focus')


