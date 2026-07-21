import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
emergency_number = os.getenv("EMERGENCY_PHONE")

client = Client(account_sid, auth_token)

def send_sms():
    message = client.messages.create(
        body="🚨 Emergency! Secret Code Detected. Please help immediately.",
        from_=twilio_number,
        to=emergency_number
    )

    print("SMS Sent Successfully!")
    print("Message SID:", message.sid)