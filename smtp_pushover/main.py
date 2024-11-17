import os
import asyncio
from smtp_pushover.email_handler import EmailHandler, start_smtp_server
from smtp_pushover.pushover_notifier import PushoverNotifier

def main():
    pushover_user_key = os.getenv("PUSHOVER_USER_KEY")
    pushover_api_token = os.getenv("PUSHOVER_API_TOKEN")

    if not pushover_user_key or not pushover_api_token:
        raise ValueError("Pushover credentials are missing. Set PUSHOVER_USER_KEY and PUSHOVER_API_TOKEN.")

    notifier = PushoverNotifier(pushover_user_key, pushover_api_token)
    email_handler = EmailHandler(notifier)

    # Start the SMTP server
    asyncio.run(start_smtp_server(email_handler))

if __name__ == "__main__":
    main()
