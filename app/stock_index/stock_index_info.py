import tushare as ts

def get_stock_index_table():
    TRANS = {"code": "指数代码",
             "name": "指数名称",
             "change": "涨跌幅",
             "open": "开盘点位",
             "preclose": "昨日收盘点位",
             "close": "收盘点位",
             "high": "最高点位",
             "low": "最低点位",
             "volume": "成交量(手)",
             "amount": "成交金额（亿元",
             }
    total = ts.get_index().to_csv().split()
    head = [TRANS.get(i) for i in total[0].split(",")]
    body = [line.split(",") for line in total[1:]]
    return {"head": head, "body": body}
