__all__ = ["StocksReportJson"]
from .stock_report_info import *
from flask import request
from flask_restful import Resource


class StocksReportJson(Resource):

    def get(self):
        year = request.args.get("year")
        season = request.args.get("season")
        return get_stock_report_json(year,season)
