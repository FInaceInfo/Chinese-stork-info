from . import wsapp,socketio,api,download
import json
wsapp.testing = True
api.testing = True
download.testing = True
class TestStockIndex(object):

    def test_index_json(self):
        client = api.test_client()
        received = client.get("/api/stocks/cn/index")
        keys = json.loads(str(received.data,"utf-8")).keys()
        assert "name" in keys

    def test_index_table(self):
        client = socketio.test_client(wsapp, namespace='/stocks-index')
        client.emit('cn_index_table', {"query":"ok"}, namespace='/stocks-index')
        received = client.get_received('/stocks-index')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'cn_index_table'
        assert type(received[0]['args'][0]) == dict

    def test_index_csv(self):
        client = download.test_client()
        received = client.get("/download/stocks/cn/index")
        data = str(received.data,"utf-8")
        assert data[:10]==",code,name"
