from sanic import Blueprint
from sanic.response import json, text, html
from sanic.exceptions import NotFound, abort
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('my_app', 'templates'))

main = Blueprint('main', url_prefix='/')


@main.exception(NotFound)
async def four_o_four(request, exception):
    template = env.get_template('main/404.html')
    content = template.render()
    return html(content, 404)

@main.route('/')
async def index(request):
    template = env.get_template('main/index.html')
    content = template.render(some_text='YAY - this is working!')
    return html(content)

@main.route('/json')
async def index_json(request):
    return json({'main_index_json': 'JSON response'})

@main.route('/text')
async def index_text(request):
    return text('main_index_text TEXT response')