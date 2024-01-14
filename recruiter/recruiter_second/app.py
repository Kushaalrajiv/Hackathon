from flask import Flask, render_template, request, jsonify
import pandas as pd
import base64
import os
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime  

app = Flask(__name__)


def get_gmail_service():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    token_path = 'token1.json'
    creds = None

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('secret_key.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def gmail_send_message(service, to_emails):
    try:
        message = EmailMessage()
        message.set_content("You have been selected to the Final Interview round! Congratulations! Please check your calendar for invite schedule")
        message["To"] = ", ".join(to_emails)  
        message["From"] = "kushaalrajiv@gmail.com"
        message["Subject"] = "Selected for Interview!"

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}

        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Message Id: {send_message["id"]}')

    except Exception as e:
        print(f"An error occurred: {e}")
        send_message = None


def get_calendar_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    creds = None
    if os.path.exists('calendar_token.json'):
        creds = Credentials.from_authorized_user_file('calendar_token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('calendar_token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)


def create_event(service):
    
    event_start = datetime.datetime(2024, 1, 20, 10, 0, 0)  
    event_end = datetime.datetime(2024, 1, 20, 11, 0, 0)

    event = {
        'summary': 'Interview with Final Candidates',
        'location': 'Virtual Meeting',
        'description': 'Discuss project details',
        'start': {
            'dateTime': event_start.isoformat(),
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': event_end.isoformat(),
            'timeZone': 'America/New_York',
        },
        'attendees': [
            {'email': 'kushaalrajiv9@gmail.com'},
            {'email': 'bindutaragolli@gmail.com'}
            
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 10},
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

# Flask routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shortlist', methods=['POST'])
def shortlist_and_send_email():
    try:
        
        df = pd.read_csv('score.csv')
        df_sorted = df.sort_values(by='Score', ascending=False)
        best_two_people = df_sorted.head(2)
        best_emails = best_two_people['email'].tolist()
        recipients = best_emails

        gmail_service = get_gmail_service()
        gmail_send_message(gmail_service, recipients)

        calendar_service = get_calendar_service()
        create_event(calendar_service)

        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
