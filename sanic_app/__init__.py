from sanic import Sanic
from sanic.response import json


def create_app():
    app = Sanic()

    @app.route('/')
    async def test(request):
        return json({'hello': 'world'})

    return app
