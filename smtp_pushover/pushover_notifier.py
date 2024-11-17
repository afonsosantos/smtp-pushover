import requests

class PushoverNotifier:
    def __init__(self, user_key: str, api_token: str):
        self.user_key = user_key
        self.api_token = api_token
        self.api_url = "https://api.pushover.net/1/messages.json"

    def send_notification(self, subject: str, body: str):
        """Send a notification with the subject as the title and the body as the message."""
        if not self.user_key or not self.api_token:
            print("Pushover credentials are missing!")
            return

        data = {
            "token": self.api_token,
            "user": self.user_key,
            "title": subject,
            "message": body,
            "priority": 1,
        }

        response = requests.post(self.api_url, data=data)
        if response.status_code == 200:
            print("Pushover notification sent successfully.")
        else:
            print(f"Failed to send Pushover notification: {response.status_code}, {response.text}")
