__all__ = ["get_stock_basics_json"]

import tushare as ts

def get_stock_basics_json():
    return ts.get_stock_basics().to_json()
