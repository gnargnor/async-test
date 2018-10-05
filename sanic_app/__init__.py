import os
from sanic import Sanic
from sanic.response import json
from .nasa import phone_home

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')


def create_app():
    app = Sanic()
    app.static('/static', STATIC_FOLDER)
    app.static('/favicon.ico', os.path.join(STATIC_FOLDER, 'img', 'favicon.ico'))
    phone_home()

    @app.route('/')
    async def test(request):
        return json({'hello': 'world'})

    return app
