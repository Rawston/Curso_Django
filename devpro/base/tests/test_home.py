from multiprocessing.connection import Client
from urllib import response

def test_status_code(client: Client):
    resp = client.get('/')
    assert response.status_code == 200