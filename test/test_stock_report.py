from . import app,socketio

class TestStockReport(object):

    def test_report_json(self):
        client = socketio.test_client(app, namespace='/stocks-report')
        client.emit('report_json', {'year': '2016',"season":"1"}, namespace='/stocks-report')
        received = client.get_received('/stocks-report')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'report_json'
        assert received[0]['args'][0].get("name").get(0) == "博天环境"

    def test_report_table(self):
        client = socketio.test_client(app, namespace='/stocks-report')
        client.emit('report_table', {'year': '2016',"season":"1"}, namespace='/stocks-report')
        received = client.get_received('/stocks-report')
        assert len(received) == 1
        assert len(received[0]['args']) == 1
        assert received[0]['name'] == 'report_table'
        assert type(received[0]['args'][0]) == dict
