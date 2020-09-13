import requests


url = "http://127.0.0.1:5000/send"


name = input('Enter your name: ')
while True:
    text = input()
    data = {'name': name, 'text': text}
    response = requests.post(url, json=data)
