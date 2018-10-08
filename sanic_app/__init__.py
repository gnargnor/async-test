import os
from dotenv import load_dotenv
load_dotenv()
from sanic import Sanic
from sanic.response import json
from .nasa import get_all_epic_urls, lookup_all_epic_dates

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')


def create_app():
    app = Sanic()
    app.static('/static', STATIC_FOLDER)
    app.static('/favicon.ico', os.path.join(STATIC_FOLDER, 'img', 'favicon.ico'))
    urls = get_all_epic_urls()
    metadata = lookup_all_epic_dates(urls)


    @app.route('/')
    async def test(request):
        return json({'hello': 'world'})

    return app
