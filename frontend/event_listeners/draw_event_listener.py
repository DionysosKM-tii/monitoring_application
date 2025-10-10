from nicegui import ui, events
from clients.api_client import api_client



def save_area_to_backend(geometry: dict) -> bool:
    """Save area geometry to backend and handle response."""
    try:
        response = api_client.post_area(geometry)
        area_id = response.get('area_id', 'Unknown')
        ui.notify(f'Area saved successfully! ID: {area_id}', type='positive')
        return True
        
    except Exception as e:
        ui.notify(f'Failed to save area: {str(e)}', type='negative')
        return False

def handle_draw(e: events.GenericEventArguments):
    """Handle drawing events on the map and save to backend."""
 
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
    
    ui.notify(f'Saving area...', type='info')
    save_area_to_backend(geometry)