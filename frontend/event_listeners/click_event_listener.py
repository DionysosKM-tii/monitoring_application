from nicegui import ui, events
from components.sidebar import update_drawer_content
from shapely.geometry import Point, Polygon as ShapelyPolygon

# Event phase constants
AT_TARGET = 2  # Direct click on map
BUBBLING_PHASE = 3  # Click bubbled from polygon/area

async def handle_click(drawer, e: events.GenericEventArguments):
    """Handle map clicks to toggle sidebar based on click target."""
    
    event_phase = e.args.get('eventPhase')
    m = e.sender  # The map instance

    if event_phase == BUBBLING_PHASE:
        # Clicked on a polygon - need to figure out which one
        
        # Get pixel coordinates from the event
        client_x = e.args.get('clientX')
        client_y = e.args.get('clientY')
        
        # Use run_map_method to convert pixel coords to lat/lng
        # This requires calling the JavaScript method on the leaflet map
        result = await m.run_map_method(
            'containerPointToLatLng',
            [client_x, client_y]
        )
        
        click_point = Point(result.get('lng'), result.get('lat'))  # Shapely uses (x, y) = (lng, lat)
        
        # Check which polygon contains this point
        clicked_layer_id = None
        for layer in m.layers:
            if hasattr(layer, 'name') and layer.name == 'polygon':
                # Get coordinates from the layer (lat, lng format)
                coords = layer.args[0]
                # Convert to (lng, lat) for Shapely
                shapely_coords = [(lng, lat) for (lat, lng) in coords]
                polygon = ShapelyPolygon(shapely_coords)
                
                if polygon.contains(click_point):
                    clicked_layer_id = layer.id
                    break
        
        # Look up and display area info
        if clicked_layer_id and not drawer.value:
            area_info = m.area_info.get(clicked_layer_id)
            if area_info:
                drawer.toggle()
                update_drawer_content(drawer, area_info)
    
    elif event_phase == AT_TARGET:
        # Clicked directly on map - close drawer if open
        if drawer.value:
            drawer.toggle()
