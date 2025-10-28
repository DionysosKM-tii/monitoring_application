from nicegui import ui
from frontend.components.map_component import create_map, load_existing_areas_on_map
from frontend.components.sidebar import create_sidebar


@ui.page('/')
async def home_page():
    """Main page with monitoring map interface."""
    
    try:
        create_sidebar()
        m = create_map()
        load_existing_areas_on_map(m)
        
    except Exception as e:
        ui.notify(f'Failed to initialize map: {str(e)}', type='negative')


    ui.notify('Map initialized successfully', type='positive')


##

      


# Tip: reload=False avoids duplicate draw toolbars during dev hot-reload
ui.run(reload=False)
