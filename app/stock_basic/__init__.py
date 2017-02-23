__all__ = ["StocksBasic"]
from .stock_basic_info import *
from flask_socketio import Namespace, emit

class StocksBasic(Namespace):

    def on_cn_basic_table(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_basic_table', get_stock_basics_table())
