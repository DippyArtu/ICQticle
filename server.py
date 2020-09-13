import chat_bot
import time
from flask import Flask, request, abort
from datetime import datetime


app = Flask(__name__)
database = []


@app.route("/")
def hello():
    return "Welcome to the ICQticle messenger server <a href='/status'>Check status</a>"


@app.route("/status")
def status():
    date = datetime.now()
    return {
        'status': True,
        'name': 'ICQticle',
        'time': date.strftime('%d.%m.%Y %H:%M:%S'),
        'messages_count': len(database),
        'users_count': len(set(message['name'] for message in database)),
         }


@app.route("/send", methods=['POST'])
def send():
    data = request.json

    if data['text'][0] == '/':
        command = data['text']
        chat_bot.bot(command, database)
    else:
        database.append({
            'id': len(database),
            'name': data['name'],
            'text': data['text'],
            'timestamp': time.time()
        })
    return{'ok': True}


@app.route("/messages")
def messages():
    if 'after_timestamp' in request.args:
        after_timestamp = float(request.args['after_timestamp'])
    else:
        after_timestamp = 0
    max_limit = 100
    if 'limit' in request.args:
        limit = int(request.args['limit'])
        if limit > max_limit:
            abort(400, 'limit is reached')
    else:
        limit = max_limit
    after_id = 0
    for message in database:
        if message['timestamp'] > after_timestamp:
            break
        after_id += 1

    return {'messages': database[after_id:after_id + limit]}


app.run()
