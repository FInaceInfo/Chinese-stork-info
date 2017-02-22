__all__ = ["StocksBasicTable", "StocksBasicJson", "StocksBasicCsv"]
from .stock_basic_info import get_stock_basics_table, get_stock_basics_json, get_stock_basics_csv
from flask_restful import Resource
from flask.views import MethodView
from flask import make_response


class StocksBasicTable(Resource):

    def get(self):
        return get_stock_basics_table()


class StocksBasicJson(Resource):

    def get(self):
        return get_stock_basics_json()


class StocksBasicCsv(MethodView):

    def get(self):
        response = make_response(get_stock_basics_csv())
        response.headers[
            "Content-Disposition"] = "attachment; filename=stocks_basic.csv;"
        return response
