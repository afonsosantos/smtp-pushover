from aiosmtpd.controller import Controller
from email import message_from_bytes
from pushover_notifier import PushoverNotifier
import asyncio

class EmailHandler:
    def __init__(self, notifier: PushoverNotifier):
        self.notifier = notifier

    async def handle_DATA(self, server, session, envelope):
        msg = message_from_bytes(envelope.content)
        subject = msg['Subject'] or "No Subject"
        body = msg.get_payload(decode=True).decode('utf-8', errors='replace')

        print(f"Received email with subject: {subject}")
        self.notifier.send_notification(subject, body)
        return '250 OK'

async def start_smtp_server(handler):
    controller = Controller(handler, hostname='0.0.0.0', port=1025)
    controller.start()
    print("SMTP server running on port 1025...")
    await asyncio.Event().wait()
