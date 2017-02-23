__all__=["get_stock_report_csv"]

import tushare as ts

def get_stock_report_csv(year, season):
    return ts.get_report_data(int(year), int(season)).to_csv()
