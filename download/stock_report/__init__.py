__all__ = ["StocksReportCsv"]
from .stock_report_info import *
from flask.views import MethodView
from flask import make_response
from flask import request


class StocksReportCsv(MethodView):

    def get(self):
        year = request.args.get("year")
        season = request.args.get("season")
        response = make_response(get_stock_report_csv(year=year,season=season))
        response.headers[
            "Content-Disposition"] = "attachment; filename=stocks_cn_report_{year}_{season}.csv;".format(
            year=year, season=season)
        return response
