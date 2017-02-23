from flask import Flask
from flask_socketio import SocketIO
from .stock_basic import *
from .stock_report import *
from .stock_index import *

app = Flask(__name__)
socketio = SocketIO(app)


socketio.on_namespace(StocksReport('/stocks-report'))
socketio.on_namespace(StocksBasic('/stocks-basic'))
socketio.on_namespace(StocksIndex('/stocks-index'))
