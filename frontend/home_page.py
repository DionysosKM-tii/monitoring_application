from nicegui import ui

from frontend.components.map_component import create_map, load_existing_areas_on_map
from frontend.components.sidebar import create_sidebar


@ui.page('/')
async def home_page():
    """Main page with monitoring map interface."""

    # Make the map 100% of the screen
    ui.query('body').style('margin: 0; padding: 0; overflow: hidden;')
    ui.query('.nicegui-content').style('padding: 0; height: 100vh; width: 100vw;')

    try:
        create_sidebar()
        m = create_map()
        load_existing_areas_on_map(m)

    except Exception as e:
        ui.notify(f'Failed to initialize map: {str(e)}', type='negative')


# Tip: reload=False avoids duplicate draw toolbars during dev hot-reload
ui.run(reload=False)
