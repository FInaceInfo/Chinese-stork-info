from . import app,socketio
import json
app.testing = True
class TestStockReport(object):

    def test_basic_json(self):
        client = app.test_client()
        received = client.get("/api/stocks")
        keys = json.loads(str(received.data,"utf-8")).keys()
        print(keys)
        assert "name" in keys

    def test_basic_table(self):
        client = app.test_client()
        received = client.get("/stocks")
        keys = json.loads(str(received.data,"utf-8")).keys()
        print(keys)
        assert "head" in keys

    def test_basic_csv(self):
        client = app.test_client()
        received = client.get("/csv/stocks")
        data = str(received.data,"utf-8")
        assert data[:10]=="code,name,"
