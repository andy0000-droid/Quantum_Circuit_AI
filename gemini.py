"""
gemini.py
This module contains a function to read an API key from a file named ".API_KEY" in the current working directory.
It is designed to be used in a Python script or module where the API key is needed for authentication or access to a service.
"""

import os


def get_api_key():
    """
    Reads the API key from a file named ".API_KEY" in the current working directory.
    :return: The API key as a string.
    """
    with open(os.path.join(os.getcwd(), ".API_KEY"), "r", encoding="UTF-8") as key_file:
        return key_file.read()


if __name__ == "__main__":
    # Test the function
    print("API Key:", get_api_key())
