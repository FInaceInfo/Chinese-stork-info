from . import wsapp,socketio,api,download
import json
wsapp.testing = True
api.testing = True
download.testing = True
class TestStockBasic(object):

    def test_basic_json(self):
        client = api.test_client()
        received = client.get("/api/stocks/cn/basic")
        keys = json.loads(str(received.data,"utf-8")).keys()
        print(keys)
        assert "name" in keys

    def test_basic_table(self):
        client = socketio.test_client(wsapp, namespace='/stocks-basic')
        client.emit('cn_basic_table', {"query":"ok"}, namespace='/stocks-basic')
        received = client.get_received('/stocks-basic')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_basic_table'
        assert type(received[0]['args'][0]) == dict

    def test_basic_csv(self):
        client = download.test_client()
        received = client.get("/download/stocks/cn/basic")
        data = str(received.data,"utf-8")
        assert data[:10]=="code,name,"
