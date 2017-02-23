__all__ = ["StocksBasicCsv"]
from .stock_basic_info import *
from flask.views import MethodView
from flask import make_response

class StocksBasicCsv(MethodView):

    def get(self):
        response = make_response(get_stock_basics_csv())
        response.headers[
            "Content-Disposition"] = "attachment; filename=stocks_basic.csv;"
        return response
