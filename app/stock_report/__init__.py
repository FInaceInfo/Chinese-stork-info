__all__ = ["StocksReport"]
from .stock_report_info import get_stock_report_table, get_stock_report_json
from flask_socketio import Namespace, emit

class StocksReport(Namespace):

    def on_report_table(self,date):
        year = date.get("year")
        season = date.get("season")
        emit('report_table', get_stock_report_table(year,season))

    def on_report_json(self,date):
        year = date.get("year")
        season = date.get("season")
        emit('report_json', get_stock_report_json(year,season))
