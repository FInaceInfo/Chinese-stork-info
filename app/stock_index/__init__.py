__all__ = ["StocksIndex"]
from .stock_index_info import *
from flask_socketio import Namespace, emit

class StocksIndex(Namespace):
    """大盘指数行情列表
    获取大盘指数实时行情列表，以表格的形式展示大盘指数实时行情。

    返回值说明：

    code:指数代码
    name:指数名称
    change:涨跌幅
    open:开盘点位
    preclose:昨日收盘点位
    close:收盘点位
    high:最高点位
    low:最低点位
    volume:成交量(手)
    amount:成交金额（亿元）
    """

    def on_cn_index_table(self,date):
        ok = date.get("query")
        if ok == "ok":
            emit('cn_index_table', get_stock_index_table())
