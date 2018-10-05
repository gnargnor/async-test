import os
from sanic_app import create_app
from dotenv import load_dotenv
load_dotenv()


print(os.environ['NASA_API_KEY'])

app = create_app()

if __name__ == '__main__':
    print('Sanic Heg Hog -- Local Debug Mode')
    app.run(host='0.0.0.0', port=7001, debug=True)


