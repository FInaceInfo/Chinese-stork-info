import tushare as ts


def get_stock_index_json():
    return ts.get_index().to_json()
