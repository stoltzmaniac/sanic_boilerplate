from sanic import Blueprint
from sanic.response import json, text


users = Blueprint('users', url_prefix='/users')


@users.route('/')
async def index(request):
    return json({'user_index': 'page'})


@users.route('/json/<word>')
async def index_json(request, word):
    return json({'user_index_json_response': word})


@users.route('/text/<word>')
async def index_text(request, word):
    return text('user_index_text TEXT ' + word)