import os
from sanic import Sanic
from sanic.response import json

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')

# the static file serving is only used during debugging



def create_app():
    app = Sanic()
    app.static('/static', STATIC_FOLDER)
    app.static('/favicon.ico', os.path.join(STATIC_FOLDER, 'img', 'favicon.ico'))

    @app.route('/')
    async def test(request):
        return json({'hello': 'world'})

    return app
