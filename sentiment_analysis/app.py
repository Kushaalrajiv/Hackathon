from flask import Flask, render_template, request, jsonify, session
from nltk.sentiment import SentimentIntensityAnalyzer
import os

app = Flask(__name__)
app.secret_key = '1612506056655a218fe5a2498ac90b27'

sia = SentimentIntensityAnalyzer()

questions = [
    "",
    "What is your name?",
    "Do you agree to work 30 hours a week?",
    "Do you agree to work in hybrid mode?",
    "Can you commute to the office considering the work location is in Bangalore?",
    "Are you open to occasional travel for work-related purposes?",
    "Can you provide the main context of your Cover Letter in 200 words.[Strictly do not exceed word limit] ",
    "Thank you for your response, we will send you a mail shortly.Type 'end' to end"
]

file_path = "sentiment_scores.txt"

@app.before_request
def before_request():
    if not hasattr(session, 'initialized'):
        with open(file_path, "a") as output_file:
            output_file.write("")
        session.cumulative_score = 0
        session.initialized = True

@app.route('/')
def home():
    session.pop('current_question_index', None)
    session['current_question_index'] = 0
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_msg = request.form['msg']

    if len(user_msg.split()) > 201:
        return jsonify({'error': 'Input exceeds 200 words. Please provide a shorter response.'}), 400

    sentiment_score = sia.polarity_scores(user_msg)['compound']
    session.cumulative_score += sentiment_score

    with open(file_path, "a") as output_file:
        output_file.write(f"{sentiment_score}\n")

    session['current_question_index'] += 1

    if session['current_question_index'] < len(questions):
        return jsonify({'question': questions[session['current_question_index']], 'sentiment': sentiment_score})
    else:
        return jsonify({'cumulative_score': session.cumulative_score}), 400

if __name__ == "__main__":
    app.run(debug=True)
