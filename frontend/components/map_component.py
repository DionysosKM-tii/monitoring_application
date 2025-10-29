from nicegui import ui
from nicegui.events import GenericEventArguments
from shapely import Point
from shapely.geometry.polygon import Polygon

from frontend.clients.api_client import api_client
from frontend.components.dtos.area_details_dto import AreaDetailsDTO
from frontend.event_listeners.draw_event_listener import handle_draw
from frontend.event_listeners.map_event_listener import on_area_selected, on_area_deselected

AREAS: list[dict] = []


def load_existing_areas_on_map(map_instance):
    """Load all saved areas and display them on the map."""
    try:

        AREAS.clear()

        areas = api_client.get_all_areas()

        for area in areas:
            area_geometry = area['geometry']

            coords = area_geometry['coordinates'][0]  # Get coordinate ring
            # Add the area to a global list, which we can retrieve later during the `.on('map-click')` event
            AREAS.append(
                {
                    "area_id": area['id'],
                    "area_name": area['name'],
                    "area_coords": coords[:-1]  # Skip duplicate last point
                }
            )
            nicegui_coords = [(lat_lng[1], lat_lng[0]) for lat_lng in coords[:-1]]

            map_instance.generic_layer(
                name='polygon',
                args=[nicegui_coords]
            )


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

    m = ui.leaflet(center=(31.5017, 34.4668), zoom=10, draw_control=draw_control)
    m.classes('w-full h-screen')

    # Register event handlers
    m.on('draw:created', handle_draw)
    m.on('draw:edited', lambda: ui.notify('Edit completed'))
    m.on('draw:deleted', lambda: ui.notify('Delete completed'))
    m.on('map-click', on_map_click)

    return m


def on_map_click(e: GenericEventArguments) -> None:
    latlng = e.args.get('latlng', {})
    if not latlng:
        return

    clicked_point = Point(latlng['lng'], latlng['lat'])

    for area in AREAS:
        polygon = Polygon(area['area_coords'])
        # An area was clicked
        if polygon.contains(clicked_point):
            on_area_selected(AreaDetailsDTO(area['area_id'], area['area_name']))
            return
    # No area was clicked
    on_area_deselected()
