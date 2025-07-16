"""
discord_notify.py
This module contains a function to send notifications to a Discord channel using a webhook.
It is designed to be used in a Python script or module where notifications are needed, such as for alerts or updates.
"""

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
api_path = os.path.join(project_root, "API")
if api_path not in sys.path:
    sys.path.append(api_path)

try:
    from APIKeyLoader import APIKeyLoader

    APIKeyLoader = APIKeyLoader()
except ImportError as e:
    print(
        "Could not import 'apikey_loader'. Please check that '../API/apikey_loader.py' exists."
    )
    raise e

try:
    import requests
except ImportError:
    print(
        "The 'requests' library is not installed. Please install it using 'pip install requests'."
    )
    raise


class DiscordNotify:
    """
    A class to handle Discord notifications.
    """

    def __init__(self):
        """Initializes the DiscordNotify class with the webhook URL and user ID."""
        self.webhook_url = APIKeyLoader.get_key("Discord_Webhook")
        self.user_id = APIKeyLoader.get_key("Discord_UID")

    def send(self, message: str, mention: bool = False):
        """
        Sends a notification to a Discord channel using the webhook URL.
        :param message: The message to send to the Discord channel.
        """
        _message = f"<@{self.user_id}> {message}" if mention else message
        data = {"content": _message}
        response = requests.post(self.webhook_url, json=data, timeout=5)
        if response.status_code == 204:
            # print("Notification sent successfully!")
            pass
        else:
            print(f"Failed to send notification. Status code: {response.status_code}")


if __name__ == "__main__":
    notifier = DiscordNotify()
    TEST_MESSAGE = "This is a test notification from the DiscordNotify module."
    notifier.send(TEST_MESSAGE)
    notifier.send(TEST_MESSAGE, mention=True)
    print("Test notification sent.")
