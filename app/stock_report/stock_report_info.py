import tushare as ts
import json

def get_stock_report_json(year, season):
    return ts.get_report_data(int(year), int(season)).to_dict()


def get_stock_report_table(year, season):
    TRANS = {"code": "代码",
             "name": "名称",
             "esp": "每股收益",
             "eps_yoy": "每股收益同比(%)",
             "bvps": "每股净资产",
             "roe": "净资产收益率(%)",
             "epcf": "每股现金流量(元)",
             "net_profits": "净利润(万元)",
             "profits_yoy": "净利润同比(%)",
             "distrib": "分配方案",
             "report_date": "发布日期"
             }
    total = ts.get_report_data(int(year), int(season)).to_csv().split()
    head = [TRANS.get(i) for i in total[0].split(",")]
    body = [line.split(",") for line in total[1:]]
    return {"head": head, "body": body}
