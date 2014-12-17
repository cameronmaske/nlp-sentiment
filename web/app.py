from flask import Flask, request, jsonify
from twython import Twython
from textblob import TextBlob
import json

app = Flask(__name__)


with open('twitter_creds.json') as f:
    creds = json.load(f)


twitter = Twython(**creds)


def avg(l):
    try:
        return sum(l) / len(l)
    except ZeroDivisionError:
        return 0


@app.route("/api/analyze/", methods=['POST'])
def analyze():
    topic = request.json.get('topic')
    tweets = twitter.search(q=topic, result_type='popular', count=100)
    sentiment = []
    subjectivity = []

    extreme = {
        'score': 0,
        'content': None
    }

    for tweet in tweets['statuses']:
        blob = TextBlob(tweet['text'])
        sentiment.append(blob.sentiment.polarity)
        subjectivity.append(blob.sentiment.subjectivity)
        if abs(blob.sentiment.polarity) > extreme['score']:
            extreme['score'] = blob.sentiment.polarity
            extreme['content'] = tweet['text']

    sentiment = avg(sentiment)
    subjectivity = avg(subjectivity)

    if sentiment == 0:
        result = "neutral"
    elif sentiment > 0:
        result = "positive"
    else:
        result = "negative"

    return jsonify(
        result=result,
        sentiment=sentiment,
        subjectivity=subjectivity,
        example=extreme)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)


