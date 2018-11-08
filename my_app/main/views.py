from sanic import Blueprint
from sanic.response import json, text, html
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('my_app', 'templates'))

main = Blueprint('main', url_prefix='/')

@main.route('/')
async def index(request):
    template = env.get_template('base.html')
    content = template.render(some_text='YAY - this is working!')
    return html(content)

@main.route('/json')
async def index_json(request):
    return json({'main_index_json': 'JSON response'})

@main.route('/text')
async def index_text(request):
    return text('main_index_text TEXT response')