__all__ = ["get_stock_basics_json",
           "get_stock_basics_csv", "get_stock_basics_csv"]

import tushare as ts


def get_stock_basics_json():
    return ts.get_stock_basics().to_json()


def get_stock_basics_table():
    TRANS = {"code": "代码",
             "name": "名称",
             "industry": "所属行业",
             "area": "地区",
             "pe": "市盈率",
             "outstanding": "流通股本(亿)",
             "totals": "总股本(亿)",
             "totalAssets": "总资产(万)",
             "liquidAssets": "流动资产",
             "fixedAssets": "固定资产",
             "reserved": "公积金",
             "reservedPerShare": "每股公积金",
             "esp": "每股收益",
             "bvps": "每股净资",
             "pb": "市净率",
             "timeToMarket": "上市日期",
             "undp": "未分利润",
             "perundp": "每股未分配",
             "rev": "收入同比(%)",
             "profit": "利润同比(%)",
             "gpr": "毛利率(%)",
             "npr": "净利润率(%)",
             "holders": "股东人数"
             }
    total = ts.get_stock_basics().to_csv().split()
    head = [TRANS.get(i) for i in total[0].split(",")]
    body = [line.split(",") for line in total[1:]]
    return {"head": head, "body": body}


def get_stock_basics_csv():
    return ts.get_stock_basics().to_csv()