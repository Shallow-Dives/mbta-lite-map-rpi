from dotenv import load_dotenv
import os
import requests

from map_controller.overlay import brightness_overlay

load_dotenv()


def test_api_payload():
    map_api_url: str = os.getenv('API_URL')
    response = requests.post(map_api_url,
                             json=brightness_overlay,
                             headers={"Content-Type": "application/json", })
