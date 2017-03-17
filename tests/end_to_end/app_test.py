import socket
import requests


def test_main_route():
    ip = socket.gethostbyname("web")
    result = requests.get('http://'+ip)
    assert result.status_code == 200
    assert result.text == 'Hello'

