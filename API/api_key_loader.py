"""
APIKeyLoader.py - A module to load API keys from a JSON file.
This module defines the APIKeyLoader class, which is responsible for loading API keys
from a JSON file named "apikey.json" located in the API directory.
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
        self.key_list = None
        self.data = None

        try:
            with open(self.filename, "r", encoding="UTF-8") as f:
                self.data = json.load(f)
                self.key_list = list(self.data.keys())

        except FileNotFoundError as e:
            print("파일을 찾을 수 없습니다.")
            raise FileNotFoundError(
                "API key file not found. Please ensure 'apikey.json' exists in the API directory."
            ) from e

        except UnicodeDecodeError as e:
            print(f"인코딩 오류: {e}")  # 파일 인코딩 확인
            raise UnicodeDecodeError("Encoding error in API key file.") from e

        except json.JSONDecodeError as e:
            print(f"JSON 문법 오류: {e.msg} (line {e.lineno}, col {e.colno})")
            raise json.JSONDecodeError(
                "Invalid JSON format in API key file.", e.doc, e.pos
            ) from e

        except OSError as e:
            print(f"I/O 오류: {e}")
            raise OSError("I/O error while accessing the API key file.") from e

    def get_key(self, key: str) -> str | None:
        """
        Returns the API key for the specified service.
        :param key: The name of the service (e.g., 'Qiskit', 'Gemini').
        :return: The API key for the specified service.
        """
        if key not in self.key_list:
            raise KeyError(f"'{key}' is not a valid API key name.")
        return self.data.get(key)["apikey"]

    def help(self):
        """
        Prints the help message for the APIKeyLoader class.
        """
        print("APIKeyLoader is used to load API keys from a JSON file.")
        print("You can use the following methods:")
        print("1. get_key(key): Returns the API key for the specified service.")
        print("2. key_list(): Returns a list of all available API keys.")
        print("3. help(): Prints this help message.")


if __name__ == "__main__":
    # Example code
    api_loader = APIKeyLoader()
    print(api_loader.key_list)
    print(api_loader.get_key("Qiskit"))  # Example for Qiskit
    api_loader.get_key("Geminasdfi")
    key_in = sys.argv[1] if len(sys.argv) > 1 else None
    print(api_loader.get_key(key_in))  # Example for command line input
