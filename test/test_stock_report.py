from . import wsapp,socketio,api,download
import json
wsapp.testing = True
api.testing = True
download.testing = True
class TestStockReport(object):

    def test_report_json(self):
        client = api.test_client()
        received = client.get("/api/stocks/cn/report",query_string={"year":"2016","season":"1"})
        keys = json.loads(str(received.data,"utf-8")).keys()
        print(keys)
        assert "name" in keys

    def test_report_table(self):
        client = socketio.test_client(wsapp, namespace='/stocks-report')
        client.emit('cn_report_table', {'year': '2016',"season":"1"}, namespace='/stocks-report')
        received = client.get_received('/stocks-report')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_report_table'
        assert type(received[0]['args'][0]) == dict

    def test_report_csv(self):
        client = download.test_client()
        received = client.get("/download/stocks/cn/report",query_string={"year":"2016","season":"1"})
        data = str(received.data,"utf-8")
        print(data[:10])
        assert data[:10]==",code,name"
