from sanic import Blueprint
from sanic.response import json, text


main = Blueprint('main', url_prefix='/')

@main.route('/')
async def index(request):
    return json({'main_index': 'page'})

@main.route('/json')
async def index_json(request):
    return json({'main_index_json': 'JSON response'})

@main.route('/text')
async def index_text(request):
    return text('main_index_text TEXT response')