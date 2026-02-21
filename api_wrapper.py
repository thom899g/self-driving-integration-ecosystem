import requests
from typing import Dict, Any
import json

class APIWrapper:
    def __init__(self):
        self.api_key = None
        self.base_url = "https://api.example.com/v1"
        self.headers = {}

    def set_api_key(self, key: str) -> None:
        """Set the API key for authentication."""
        self.api_key = key
        self.headers['Authorization'] = f"Bearer {key}"
        
    def make_request(self,