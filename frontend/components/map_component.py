from nicegui import ui

from frontend.clients.api_client import api_client
from frontend.event_listeners.draw_event_listener import handle_draw


def load_existing_areas_on_map(map_instance):
    """Load all saved areas and display them on the map."""
    try:

        areas = api_client.get_all_areas()

        for area in areas:
            area_geometry = area['geometry']

            coords = area_geometry['coordinates'][0]  # Get coordinate ring
            nicegui_coords = [(lat_lng[1], lat_lng[0]) for lat_lng in
                              coords[:-1]]  # Convert [lng,lat] to (lat,lng), skip duplicate
            layer = map_instance.generic_layer(
                name='polygon',
                args=[
                    nicegui_coords,
                    {'area_id': area['id']},
                    {'area_name': area['name']}
                ]
            )

        ui.notify(f'Processed {len(areas)} areas from database', type='positive')

    except Exception as e:
        print(f"Load areas error: {e}")
        ui.notify(f'Failed to load areas: {str(e)}', type='negative')


def create_map():
    """Create and configure the main map component."""
    # Map drawing/editing controls configuration
    draw_control = {
        'draw': {
            'polygon': True,
            'marker': False,
            'circle': False,
            'rectangle': True,
            'polyline': False,
            'circlemarker': False,
        },
        'edit': {
            'edit': True,
            'remove': True,
        },
    }

    # Create the leaflet map
    m = ui.leaflet(center=(51.505, -0.09), zoom=12, draw_control=draw_control)
    # full width; height fills the viewport minus the header (approx 64px)
    m.classes('w-full h-[calc(100vh-64px)]')

    # Register event handlers
    m.on('draw:created', handle_draw)
    m.on('draw:edited', lambda: ui.notify('Edit completed'))
    m.on('draw:deleted', lambda: ui.notify('Delete completed'))

    return m
