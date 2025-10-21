from nicegui import ui
from components.map_component import create_map, load_existing_areas_on_map
from components.sidebar import create_sidebar
"""
import debugpy

# Enable debugger on port 5678
debugpy.listen(5678)
print("⏳ Waiting for debugger to attach...")
debugpy.wait_for_client()
print("✅ Debugger attached!")
"""

@ui.page('/')
async def home_page():
    """Main page with monitoring map interface."""
    
    try:
        drawer = create_sidebar()
        m = create_map(drawer)
        load_existing_areas_on_map(m)
        ui.add_head_html('''
        <style>
        /* Ensure full height for all parent containers */
        html, body {
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* Only remove top/right/bottom padding, let Quasar manage left padding for drawer */
        .q-page-container {
            padding-top: 0 !important;
            padding-right: 0 !important;
            padding-bottom: 0 !important;
            margin: 0 !important;
            transition: padding-left 0.3s ease;
            height: 100vh !important;
        }

        .q-page {
            padding: 0 !important;
            margin: 0 !important;
            min-height: 100vh !important;
            height: 100vh !important;
        }

        .nicegui-content {
            padding: 0 !important;
            margin: 0 !important;
            height: 100vh !important;
        }

        /* Ensure smooth transition */
        .nicegui-leaflet {
            transition: all 0.3s ease;
            height: 100vh !important;
        }
        </style>
        ''')


    except Exception as e:
        ui.notify(f'Failed to initialize map: {str(e)}', type='negative')


    ui.notify('Map initialized successfully', type='positive')


##

      


# Tip: reload=False avoids duplicate draw toolbars during dev hot-reload
ui.run(reload=False)
