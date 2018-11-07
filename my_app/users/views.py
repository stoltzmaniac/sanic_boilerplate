from sanic import Blueprint
from sanic.response import json, text


users = Blueprint('users', url_prefix='/users')

@users.route('/')
async def index(request):
    return json({'users_index': 'page'})

@users.route('/json')
async def index_json(request):
    return json({'users_index_json': 'JSON response'})

@users.route('/text')
async def index_text(request):
    return text('users_index_text TEXT response')