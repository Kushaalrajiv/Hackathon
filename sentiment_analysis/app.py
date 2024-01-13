from flask import Flask, render_template, request, jsonify, session
from nltk.sentiment import SentimentIntensityAnalyzer
import pickle

app = Flask(__name__)
app.secret_key = '1612506056655a218fe5a2498ac90b27'

sia = SentimentIntensityAnalyzer()


questions = [
    "",
    "What is your name?",
    "Do you agree to work 30 hours a week?",
    "Do you agree to work in hybrid mode?",
    "Do you have what it takes to collaborate and deliver good results?",
    "Can you provide the main context of your Cover Letter ",
    "Thank you for your response, we will send you a mail shortly.Type 'end' to end"
]

output_file = open("sentiment_scores.txt", "w")

@app.route('/')
def home():
    session.pop('current_question_index', None)
    session['current_question_index'] = 0
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_msg = request.form['msg']

    sentiment_score = sia.polarity_scores(user_msg)['compound']

    output_file.write(f"Question {session['current_question_index'] + 1}: {sentiment_score}\n")

    print(f"Question {session['current_question_index'] + 1}: {questions[session['current_question_index']]}")

    session['current_question_index'] += 1

    if session['current_question_index'] < len(questions):
        return jsonify({'question': questions[session['current_question_index']], 'sentiment': sentiment_score})
    else:
        output_file.close()
        return jsonify({'message': "All questions have been asked. Sentiment scores are stored in sentiment_scores.txt."})

if __name__ == "__main__":
    app.run(debug=True)