from frontend.components.sidebar import sidebar_show, sidebar_hide


def on_area_selected(area: dict) -> None:
    sidebar_show(area)


def on_area_deselected() -> None:
    sidebar_hide()
