import requests
from typing import Dict, Any
import logging

class DataCollector:
    def __init__(self):
        self.data_sources = []
        self.last_error = None
        self.collected_data = {}

    def collect_real_time_data(self) -> Dict[str, Any]:
        """Collect real-time data from all registered sources."""
        try:
            collected_data = {}
            for source in self.data_sources:
                data = self._fetch_from_source(source)
                if data:
                    collected_data[source] = data
            self.collected_data = collected_data
            return collected_data
        except Exception as e:
            self.last_error = str(e)
            logging.error(f"Failed to collect data: {str(e)}")
            raise

    def _fetch_from_source(self, source_url: str) -> Dict[str, Any]:
        """Fetch data from a single data source."""
        try:
            response = requests.get(source_url, timeout=10)
            if response.status_code == 200:
                return response.json()
            logging.warning(f"Received non-200 status code {response.status_code} from {source_url}")
            raise Exception("Data fetch failed")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error fetching data from {source_url}: {str(e)}")
            raise