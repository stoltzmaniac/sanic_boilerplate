from sanic import Blueprint
from sanic.response import json, text


api = Blueprint('api', url_prefix='/api')


@api.route('/')
async def index(request):
    return json({'api_index': 'page'})


@api.route('/json/<word>')
async def index_json(request, word):
    return json({'api_index_json_response': word})


@api.route('/text/<word>')
async def index_text(request, word):
    return text('api_index_text TEXT' + word)


@api.route('/get', methods=['GET'])
async def get_handler(request):
    return text(f'GET request - {request.args}')


@api.route('/post', methods=['POST'])
async def post_handler(request):
    return text(f'POST request - {request.args}')
