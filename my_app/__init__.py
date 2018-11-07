from sanic import Sanic
from config import Config

from my_app.api.views import api
from my_app.users.views import users
from my_app.main.views import main



def create_app():
    app = Sanic()
    app.config.from_object(Config)

    app.blueprint(api)
    app.blueprint(users)
    app.blueprint(main)

    return app

