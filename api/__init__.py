from flask import Flask, make_response, json
from flask_restful import Api
from .stock_basic import *
from .stock_report import *
from .stock_index import *
app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    if isinstance(data, dict):
        resp = make_response(json.dumps(data), code)
    else:
        resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(StocksBasicJson, '/api/stocks/cn/basic')
api.add_resource(StocksReportJson, '/api/stocks/cn/report')
api.add_resource(StocksIndexJson,'/api/stocks/cn/index')
