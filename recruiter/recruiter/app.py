from flask import Flask, render_template, request, jsonify
import pandas as pd
import base64
import os
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)

def get_gmail_service():
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    token_path = 'token.json'
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
        message.set_content("You have been selected to the Second round! Congratulations! This is your Second Round Link - http://127.0.0.1:5000")
        message["To"] = ", ".join(to_emails)  # Join multiple emails with commas
        message["From"] = "kushaalrajiv@gmail.com"
        message["Subject"] = "Selected!"

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}

        send_message = service.users().messages().send(userId="me", body=create_message).execute()
        print(f'Message Id: {send_message["id"]}')

    except Exception as e:
        print(f"An error occurred: {e}")
        send_message = None

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

        return jsonify({'status': 'success'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True,port=8000)
