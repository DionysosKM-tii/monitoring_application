import requests
from typing import Dict, Any, List
from dotenv import load_dotenv
import os

load_dotenv()
BACKEND_ENDPOINT = os.getenv("BACKEND_ENDPOINT", None)

class ApiClient:
    """HTTP client for communicating with the FastAPI backend."""
    
    def __init__(self, base_url: str = BACKEND_ENDPOINT):
        self.base_url = base_url
    
    def post_area(self, geometry: Dict[str, Any], name: str = "") -> Dict[str, Any]:
        """
        Send area geometry to backend for creation.
        
        Args:
            geometry: GeoJSON geometry object
            
        Returns:
            dict: Response from backend containing area_id
            
        Raises:
            requests.RequestException: If API call fails
        """
        url = f"{self.base_url}/areas/create"
        payload = {"geometry": geometry, "name": name}
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()  # Raises exception for HTTP error codes
            return response.json()
            
        except requests.exceptions.ConnectionError:
            raise Exception("Could not connect to backend server. Is it running?")
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Backend server may be slow.")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Backend server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")

    def get_all_areas(self) -> List[Dict[str, Any]]:
        """
        Get all saved areas from backend.
        
        Returns:
            list: List of area objects with id, geometry, and name fields
            
        Raises:
            requests.RequestException: If API call fails
        """
        url = f"{self.base_url}/areas"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises exception for HTTP error codes
            
            data = response.json()
            return [item.get("geometry", item) for item in data]
            
        except requests.exceptions.ConnectionError:
            raise Exception("Could not connect to backend server. Is it running?")
        except requests.exceptions.Timeout:
            raise Exception("Request timed out. Backend server may be slow.")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Backend server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {str(e)}")

# Global API client instance
api_client = ApiClient()
