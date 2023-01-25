"""
MBTA Lite Map Controller
Display Red Line stations as LEDs representing train status
"""
from dotenv import load_dotenv
import os
import requests
import time
from typing import Dict, List, Optional, Tuple

from map_controller.utils import check_wifi_connected
from map_controller.overlay import brightness_overlay

load_dotenv()


class MapController:
    def __init__(self):
        self.wifi_detected = False
        # Define Leds
        self.num_pixels: int = 29
        self.default_display: List[Tuple] = [(255, 0, 0)] * self.num_pixels
        self.brightness_overlay = brightness_overlay
        self.map_api_url = os.getenv('API_URL')
        if os.getenv('RPI') == "true":
            import board
            import neopixel
            self.pixels = neopixel.NeoPixel(
                board.D18, self.num_pixels, brightness=0.2, auto_write=False)

    def run_controller(self):
        # Don't try the API until connected to wifi for the first time
        if self.wifi_detected:
            try:
                response = requests.post(self.map_api_url,
                                     json=self.brightness_overlay,
                                     headers={"Content-Type": "application/json"})
                leds = response.content
            except requests.exceptions.RequestException:
                leds = self.default_display

        else:
            leds = self.default_display
            self.wifi_detected = check_wifi_connected()

        for i in range(self.num_pixels):
            self.pixels[i] = leds[i]
        self.pixels.show()

        time.sleep(5)
