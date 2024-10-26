import requests
import logging

class NOAAClient:
    def __init__(self):
        self.base_url = "https://api.weather.gov"

    def get_hurricane_alerts(self):
        response = requests.get(f"{self.base_url}/alerts")
        if response.status_code != 200:
            logging.error(f"Error al obtener alertas de huracanes: {response.status_code} - {response.text}")
            return None
        return response.json()

class EarthquakeClient:
    def __init__(self):
        self.base_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

    def get_earthquake_alerts(self):
        response = requests.get(f"{self.base_url}query?format=geojson&alertLevel=red")
        if response.status_code != 200:
            logging.error(f"Error al obtener alertas de terremotos: {response.status_code} - {response.text}")
            return None
        return response.json()
