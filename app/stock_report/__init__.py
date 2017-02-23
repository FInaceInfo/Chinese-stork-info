__all__ = ["StocksReport"]
from .stock_report_info import *
from flask_socketio import Namespace, emit

class StocksReport(Namespace):

    def on_cn_report_table(self,date):
        year = date.get("year")
        season = date.get("season")
        emit('cn_report_table', get_stock_report_table(year,season))
