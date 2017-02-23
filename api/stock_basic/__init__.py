__all__ = ["StocksBasicJson"]
from .stock_basic_info import *
from flask_restful import Resource


class StocksBasicJson(Resource):

    def get(self):
        return get_stock_basics_json()
