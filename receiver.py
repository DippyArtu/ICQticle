import requests
import time
from datetime import datetime


def print_formatted(message):
    """
    2020/09/08 10:00:23  Name
    Text

    """
    dt = datetime.fromtimestamp(message['timestamp'])
    dt = dt.strftime('%Y/%m/%d %H:%M:%S')
    first_line = dt + '  ' + message['name']
    print(first_line)
    print(message['text'])
    print()


url = 'http://127.0.0.1:5000/messages'
after_timestamp = 0


while True:
    response = requests.get(url, params={'after_timestamp': after_timestamp})
    messages = response.json()['messages']
    for message in messages:
        print_formatted(message)
        after_timestamp = message['timestamp']
    if not messages:
        time.sleep(1)
