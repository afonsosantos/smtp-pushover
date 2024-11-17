import asyncio
from aiosmtpd.controller import Controller
from email import message_from_bytes
from smtp_pushover.pushover_notifier import PushoverNotifier

class EmailHandler:
    def __init__(self, notifier: PushoverNotifier):
        self.notifier = notifier

    async def handle_DATA(self, server, session, envelope):
        # Parse the email content
        msg = message_from_bytes(envelope.content)

        # Extract the subject
        subject = msg['Subject'] or "No Subject"

        # Extract the body, ignoring headers
        if msg.is_multipart():
            # If the email is multipart, extract the plain text part
            for part in msg.iter_parts():
                if part.get_content_type() == 'text/plain' and part.get_content_disposition() is None:
                    body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                    break
            else:
                body = "No plain text content found."
        else:
            # If the email is not multipart, extract the body directly
            body = msg.get_payload(decode=True).decode('utf-8', errors='replace')

        print(f"Received email with subject: {subject}")

        # Send the notification to Pushover
        self.notifier.send_notification(subject, body)
        return '250 OK'

async def start_smtp_server(handler):
    controller = Controller(handler, hostname='', port=1025)
    controller.start()
    print("SMTP server running on port 1025...")
    await asyncio.Event().wait()
