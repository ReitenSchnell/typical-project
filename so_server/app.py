import bottle
from bottle import route


@route('/')
def index():
    return ('Hello')


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080)
else:
    app = application = bottle.default_app()
