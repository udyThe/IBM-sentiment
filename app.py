from flask import Flask, render_template, request
import boto3

app = Flask(__name__)
comprehend = boto3.client(service_name='comprehend', region_name='ap-south-1')

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    scores = None

    if request.method == 'POST':
        text = request.form['text']
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
        scores = response['SentimentScore']

    return render_template('index.html', sentiment=sentiment, scores=scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
