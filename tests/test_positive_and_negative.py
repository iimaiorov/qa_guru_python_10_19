from tests.conftest import DOMAIN_URL, REGISTER_API
import requests

email = 'eve.holt@reqres.in'
password = 'pistol'


def test_successful_register():
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 200


def test_failed_register():
    payload = {
        'email': email,
    }
    response = requests.post(DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
