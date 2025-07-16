"""
discord_notify.py - A module to handle Discord notifications.
This module defines the DiscordNotify class, which is responsible for sending notifications
"""

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
api_path = os.path.join(project_root, "API")
if api_path not in sys.path:
    sys.path.append(api_path)

try:
    from api_key_loader import APIKeyLoader

    APIKeyLoader = APIKeyLoader()
except ImportError as e:
    print(
        "Could not import 'api_key_loader'. Please check that '../API/api_key_loader.py' exists."
    )
    raise e

try:
    import requests
except ImportError:
    print(
        "The 'requests' library is not installed. Please install it using 'pip install requests'."
    )
    raise

WEBHOOK_URL = APIKeyLoader.get_key("Discord_Webhook")
USER_ID = APIKeyLoader.get_key("Discord_UID")
if not WEBHOOK_URL or not USER_ID:
    raise ValueError("Discord webhook URL or user ID is not set in the API keys.")


def send_message(message: str, mention: bool = False):
    """
    Sends a notification to a Discord channel using the webhook URL.
    :param message: The message to send to the Discord channel.
    """
    _message = f"<@{USER_ID}> {message}" if mention else message
    data = {"content": _message}
    response = requests.post(WEBHOOK_URL, json=data, timeout=5)
    if response.status_code == 204:
        # print("Notification sent successfully!")
        pass
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")


if __name__ == "__main__":
    TEST_MESSAGE = "This is a test notification from the discord_notify module."
    send_message(TEST_MESSAGE)
    send_message(TEST_MESSAGE, mention=True)
    print("Test notification sent.")
