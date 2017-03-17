from so_server import app
from webtest import TestApp


def test_main_route():
    application = TestApp(app)
    resp = application.get('/')
    assert resp.status == '200 OK'
    assert resp.content_length > 0
