"""
gemini.py
This module contains a function to read an API key from a file named ".API_KEY" in the current working directory.
It is designed to be used in a Python script or module where the API key is needed for authentication or access to a service.
"""

import os
import json


def get_api_key():
    """
    Reads the API key from a file named "apikey.json" in the current working directory.

    return: The API key as a string.
    """
    key_name = list()
    key_value = list()

    with open(os.path.join(os.curdir, "apikey.json"), encoding="UTF-8") as f:
        api_keys = json.load(f)
        for api_key in api_keys:
            key_name.append(api_key.capitalize())
            key_value.append(api_keys[api_key]["key"])
    return dict(zip(key_name, key_value))


if __name__ == "__main__":
    # Test the function
    key_dict = get_api_key()
    print(key_dict)
    print(key_dict["gemini".capitalize()])
