from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def send_whatsapp_message(body):
    client.messages.create(
        body=body,
        from_=os.getenv("TWILIO_PHONE"),
        to=os.getenv("USER_PHONE")
    )
