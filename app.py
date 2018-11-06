from sanic import Sanic, Blueprint
from sanic.response import json, text


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
