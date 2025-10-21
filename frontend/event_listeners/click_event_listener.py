from nicegui import ui, events

# Event phase constants
AT_TARGET = 2  # Direct click on map
BUBBLING_PHASE = 3  # Click bubbled from polygon/area

def handle_click(drawer, e: events.GenericEventArguments):
    """Handle map clicks to toggle sidebar based on click target.
    
    - Click on area: Open drawer (or keep open if already open)
    - Click on map: Close drawer
    
    Args:
        drawer: The drawer instance to control
        e: The click event arguments
    """
    if not drawer:
        return
    
    event_phase = e.args.get('eventPhase')
    
    if event_phase == BUBBLING_PHASE:
        # Clicked on a polygon/area - open drawer if closed
        if not drawer.value:  # drawer.value is True when open, False when closed
            drawer.toggle()
        # If drawer is already open, do nothing (keep it open)
    
    elif event_phase == AT_TARGET:
        # Clicked directly on map (not on a polygon) - close drawer if open
        if drawer.value:  # drawer is open
            drawer.toggle()

