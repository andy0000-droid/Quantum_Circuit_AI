"""
discord_notify.py
This module contains a function to send notifications to a Discord channel using a webhook.
It is designed to be used in a Python script or module where notifications are needed, such as for alerts or updates.
"""

try:
    import requests
except ImportError:
    print(
        "The 'requests' library is not installed. Please install it using 'pip install requests'."
    )
    raise


def send_discord_notification(message):
    """
    Sends a notification to a Discord channel using a webhook.
    :param message: The message to send to the Discord channel.
    """
    data = {"content": message}
    webhook_url = "https://discord.com/api/webhooks/1357570178296188948/B3gq2UxdcsHne6pU8xRl5gM-sJ7ZK8cASg-6HFjqgSQX07akafV3VRPDKcMIe8TMBP2b"
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        # print("Notification sent successfully!")
        pass
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")


if __name__ == "__main__":
    TEST_MESSAGE = "Hello, this is a notification from Python!"

    send_discord_notification(TEST_MESSAGE)
