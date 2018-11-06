from sanic import Sanic
from sanic.response import json

from api.views import api
from users.views import users


app = Sanic()

@app.route('/')
async def index(request):
    return json({'index': 'page'})


@app.websocket('/feed')
async def foo3(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)


app.blueprint(api)
app.blueprint(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
