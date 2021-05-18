from flask import *
import os
import requests
import json

app = Flask(__name__)
tweetQ = []


@app.route('/tweets', methods=['GET'])
def get_tweet():
    if len(tweetQ) != 0:
        print(tweetQ[0])
        return tweetQ.pop()
    return {'status': 'empty'}


@app.route('/', methods=['POST'])
def add_tweet():
    print(request.form)
    data = request.get_data()
    data = data.decode('utf-8')
    # data = parse_tweet_stream(data)

    data = json.loads(data)
    tweetQ.append(data)
    return "GOT IT!"

def parse_tweet_stream(stream):
    tweet = {}
    stream.replace("\n", "")
    for i in stream:
        if i in tweet:
            temp = {i: {tweet}}
            del tweet[i]


app.run()
