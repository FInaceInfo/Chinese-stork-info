from flask import Flask
from flask_socketio import SocketIO
from .stock_basic import *
from .stock_report import *
from .stock_index import *

app = Flask(__name__)
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('box-office.log', maxBytes=10*1024*1024,backupCount=5)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
    
socketio = SocketIO(app)


socketio.on_namespace(StocksReport('/stocks-report'))
socketio.on_namespace(StocksBasic('/stocks-basic'))
socketio.on_namespace(StocksIndex('/stocks-index'))
