from flask import Flask
from calendar_utils import get_calendar_service
from whatsapp_utils import send_whatsapp_message
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def notify_events():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=5, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        send_whatsapp_message("No upcoming events.")
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        message = f"Upcoming: {event['summary']} at {start}"
        send_whatsapp_message(message)

    return "Events sent!"

if __name__ == '__main__':
    app.run(debug=True)
