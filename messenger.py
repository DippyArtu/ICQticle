from client_ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from datetime import datetime
import requests


class Messenger(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.url = url
        self.after_timestamp = -1

        self.text_input.returnPressed.connect(self.button_pressed)
        self.send_button.pressed.connect(self.button_pressed)

        self.load_messages()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)


    def print_formatted(self, message):
        dt = datetime.fromtimestamp(message['timestamp'])
        dt = dt.strftime('%Y/%m/%d %H:%M:%S')
        first_line = dt + '  ' + message['name']
        self.messages_browser.append(first_line)
        self.messages_browser.append(message['text'])
        self.messages_browser.append('')
        self.messages_browser.repaint()

    def update_messages(self):
        response = None
        try:
            response = requests.get(self.url + '/messages', params={'after_timestamp': self.after_timestamp})
        except:
            pass
        if response and response.status_code == 200:
            messages = response.json()['messages']
            for message in messages:
                self.print_formatted(message)
                self.after_timestamp = message['timestamp']
            return messages

    def load_messages(self):
        while self.update_messages():
            pass

    def button_pressed(self):
        name = self.name_input.text()
        text = self.text_input.text()
        data = {'name': name, 'text': text}
        response = None
        try:
            response = requests.post(self.url + '/send', json=data)
        except:
            pass
        if response and response.status_code == 200:
            self.text_input.clear()
            self.text_input.repaint()
        else:
            self.messages_browser.append('Error sending a message, server is offline')
            self.messages_browser.append('')
            self.messages_browser.repaint()


app = QtWidgets.QApplication([])
window = Messenger('ADRESS_GOES_HERE')  # -------------------- CHANGE THIS TO YOUR SERVER'S ADDRESS!!!
window.show()
app.exec_()
