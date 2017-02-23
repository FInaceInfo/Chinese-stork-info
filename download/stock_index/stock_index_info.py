import tushare as ts


def get_stock_index_csv():
    return ts.get_index().to_csv()
