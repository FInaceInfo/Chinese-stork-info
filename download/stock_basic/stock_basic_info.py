__all__ = ["get_stock_basics_csv"]

import tushare as ts

def get_stock_basics_csv():
    return ts.get_stock_basics().to_csv()
