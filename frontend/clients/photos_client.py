import os
from typing import Optional

import requests
from dotenv import load_dotenv
from nicegui import context

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


class PhotosClient:

    def __init__(self):
        self.base_url = BASE_URL

    def get_photos_for_area(self, area_id: int):
        response: Optional[requests.Response] = None
        try:
            endpoint = f"{self.base_url}/photos/{area_id}"
            response = requests.get(endpoint)
            response.raise_for_status()
            response_data = response.json()
        except Exception as e:
            #  TODO: we need to raise application specific exception
            raise Exception(f"Error fetching photos for area {area_id}: {e}")
        finally:
            if response is not None:
                response.close()

        return response_data

def get_photos_client():
    client = context.client

    if not hasattr(client, '_photos_client_instance'):
        client._photos_client_instance = PhotosClient()

    return client._photos_client_instance