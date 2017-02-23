from flask import Flask
from .stock_basic import *
from .stock_report import *
app = Flask(__name__)


app.add_url_rule('/download/stocks/cn/basic', view_func=StocksBasicCsv.as_view('csv_stocks_cn_basic'))
app.add_url_rule('/download/stocks/cn/report', view_func=StocksReportCsv.as_view('csv_stocks_cn_report'))
