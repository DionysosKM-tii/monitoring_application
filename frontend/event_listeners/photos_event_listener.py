from frontend.clients.photos_client import get_photos_client


def display_slideshow_for_area(area_id: int) -> None:
    photos_data = get_photos_client().get_photos_for_area(area_id)
    print(photos_data)