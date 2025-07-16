"""
gemini.py
This module contains a function to read an API key from a file named ".API_KEY" in the current working directory.
It is designed to be used in a Python script or module where the API key is needed for authentication or access to a service.
"""

import os
import json
import sys


class APIKeyLoader:
    """
    A class to load API keys from a JSON file.
    The file should be named "apikey.json" and located in the API directory.
    """

    def __init__(self, filename="apikey.json"):
        """
        Initializes the APIKeyLoader with the path to the JSON file containing API keys.
        :param filename: The name of the JSON file containing API keys.
        """
        self.dir = os.path.dirname(__file__)
        self.filename = os.path.join(self.dir, filename)
        self._key = None

    def __load_keys__(self):
        """
        Loads API keys from the specified JSON file.
        :return: A dictionary containing the API keys.
        """
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"{self.filename} does not exist.")

        with open(self.filename, "r", encoding="UTF-8") as file:
            return json.load(file)

    def __ret_key__(self):
        """
        Retrieves the API key for the specified service.
        :return: The API key for the specified service.
        """
        keys = self.__load_keys__()
        if self._key in keys:
            return keys[self._key]["key"]
        else:
            raise KeyError(f"API key for '{self._key}' not found.")

    def get_key(self, key: str) -> str | None:
        """
        Returns the API key for the specified service.
        :param key: The name of the service (e.g., 'Qiskit', 'Gemini').
        :return: The API key for the specified service.
        """
        self._key = key
        try:
            return self.__ret_key__()
        except KeyError as e:
            print(e)
            return None

    def Key_lists(self):
        """
        Prints all API keys list.
        """
        keys = self.__load_keys__()
        for service in keys:
            print(f"{service}")


if __name__ == "__main__":
    # Example code
    api_loader = APIKeyLoader()
    api_loader.Key_lists()
    print(api_loader.get_key("Qiskit"))  # Example for Qiskit
    api_loader.get_key("Geminasdfi")
    key_in = sys.argv[1] if len(sys.argv) > 1 else None
    print(api_loader.get_key(key_in))  # Example for command line input
