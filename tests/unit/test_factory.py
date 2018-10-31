from bank_app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    """
    Tests if application is returning a valid response to /hello url

    :param client: pytest fixture named client, located in conftest.py
    :return: None
    """
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
