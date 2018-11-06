from sanic import Sanic, Blueprint
from sanic.response import json, text

from api.views import api
from users.views import users


app = Sanic()

@app.route('/')
async def index(request):
    return json({'index': 'page'})


@app.route('/json')
async def index_json(request):
    return json({'index_json': 'JSON response'})


@app.route('/text')
async def index_text(request):
    return text('index_text TEXT response')


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
