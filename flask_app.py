#!/usr/bin/python
from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['host'] = '0.0.0.0'
socketio = SocketIO(app)

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
