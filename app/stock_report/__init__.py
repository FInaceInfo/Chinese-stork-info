

__all__ = ["StocksReport"]
from .stock_report_info import *
from flask_socketio import Namespace, emit

class StocksReport(Namespace):
    """
    业绩报告,包括:
    业绩报告（主表）
    盈利能力数据
    营运能力数据
    成长能力数据
    偿债能力数据
    现金流量数据

    都需要参数year,season
    """
    def on_cn_report_table(self,date):
        """业绩报告（主表）
        按年度,季度获取业绩报表数据.结果返回的数据属性说明如下：

        code,代码
        name,名称
        esp,每股收益
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
        """
        year = date.get("year")
        season = date.get("season")
        emit('cn_report_table', get_stock_report_table(year,season))
