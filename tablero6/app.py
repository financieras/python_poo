from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

tablero = Tablero(5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('tablero', tablero.tablero)

@socketio.on('mover_letra')
def handle_mover_letra():
    tablero.mover_letra()
    emit('tablero', tablero.tablero)

if __name__ == '__main__':
    socketio.run(app)
