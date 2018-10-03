from sanic_app import create_app

app = create_app()

if __name__ == '__main__':
    print('Sanic Heg Hog -- Local Debug Mode')
    app.run(host='0.0.0.0', port=7001, debug=True)


