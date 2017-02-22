from flask_script import Manager, Server
from server import GeventServer, TestServer,TestWsServer,WsServer
from app import app
from app import socketio
manager = Manager(app)

SERVER = {
    "test": TestServer(app=app),
    "gevent": GeventServer(app=app),
    "testws": TestWsServer(app=app,socketio=socketio),
    "ws": WsServer(app=app,socketio=socketio)
}


@manager.command
def server(choise):
    """can choose from test gevent"""
    print("server start")
    SERVER.get(choise, lambda x, y: print("unknow server"))(
        host="0.0.0.0", port=5000)

if __name__ == "__main__":
    manager.run()
