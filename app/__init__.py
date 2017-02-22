from flask import Flask, make_response, json
from flask_restful import Api
from flask_socketio import SocketIO
from .stock_basic import StocksBasicJson, StocksBasicTable, StocksBasicCsv
from .stock_report import StocksReport
app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    if isinstance(data, dict):
        resp = make_response(json.dumps(data), code)
    else:
        resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(StocksBasicTable, '/stocks')
api.add_resource(StocksBasicJson, '/api/stocks')
app.add_url_rule('/csv/stocks', view_func=StocksBasicCsv.as_view('csv_stocks'))

socketio.on_namespace(StocksReport('/stocks-report'))
