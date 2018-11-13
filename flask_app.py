#!/usr/bin/python
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO
import smbus2
import os

bus = smbus2.SMBus(1)
address = 0x04

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['host'] = '0.0.0.0'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + str(message))
    if isinstance(message, int):
        if message > -1 and message < 9:
            print("sending int " + str(message))
            bus.write_byte(address, message)
    else:
        print("message is not an int?")

@socketio.on('speak')
def handle_message(message):
    if isinstance(message, str):
        os.system("espeak '" + message + "'")
    else:
        print("message is not a string")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/js/<path:path>')
def js_files(path):
    return send_from_directory('static/js', path)

@app.route('/css/<path:path>')
def css_files(path):
    return send_from_directory('static/css', path)

@app.route('/images/<path:path>')
def image_files(path):
    return send_from_directory('static/img', path)

if __name__ == '__main__':
    socketio.run(app)
