import tushare as ts


def get_stock_report_json(year, season):
    return ts.get_report_data(int(year), int(season)).to_json()
