from sanic import Blueprint
from sanic.response import json, text


api = Blueprint('api', url_prefix='/api')

@api.route('/')
async def index(request):
    return json({'api_index': 'page'})

@api.route('/json')
async def index_json(request):
    return json({'api_index_json': 'JSON response'})

@api.route('/text')
async def index_text(request):
    return text('api_index_text TEXT response')