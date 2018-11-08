from sanic import Blueprint
from sanic.response import json, text, html
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('my_app', 'templates'))

users = Blueprint('users', url_prefix='/users')

@users.route('/')
async def index(request):
    template = env.get_template('index.html')
    content = template.render(some_text='YAY - this is working!')
    return html(content)

@users.route('/json')
async def index_json(request):
    return json({'users_index_json': 'JSON response'})

@users.route('/text')
async def index_text(request):
    return text('users_index_text TEXT response')