from nicegui import events
from components.area_popup_window.popup_window import AreaNameDialog


def handle_draw(e: events.GenericEventArguments):
    """Handle drawing events on the map and save to backend after getting area name."""
    
    layer = e.args['layer']
    
    # Extract coordinates from layer dictionary
    coords = layer['_latlngs'][0]  # Get coordinate ring
    
    # Convert to GeoJSON format [lng, lat]
    geojson_coords = [[point['lng'], point['lat']] for point in coords]
    geojson_coords.append(geojson_coords[0])  # Close polygon
    
    geometry = {
        "type": "Polygon",
        "coordinates": [geojson_coords]
    }
    
    # Show dialog with geometry
    AreaNameDialog(geometry=geometry).show()
    
