import requests
from tests.conftest import DOMAIN_URL, REGISTER_API, USERS_API, LOGIN_API
from scheme.scheme import GetUsers, CreateUser, GetUser, LoginUser, RegisterUser
from jsonschema import validate

email = 'eve.holt@reqres.in'
password = 'pistol'


def test_create_user_validate():
    payload = {
        'name': 'morpheus',
        'job': 'leader'
    }
    response = requests.post(DOMAIN_URL + USERS_API, data=payload)
    validate(instance=response.json(), schema=CreateUser)


def test_get_users_validate():
    response = requests.get(DOMAIN_URL + USERS_API, params={'page': 1})
    validate(instance=response.json(), schema=GetUsers)


def test_get_user_validate():
    response = requests.get(f'{DOMAIN_URL}{USERS_API}/2')
    validate(instance=response.json(), schema=GetUser)


def test_register_validate():
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(DOMAIN_URL + REGISTER_API, data=payload)
    validate(instance=response.json(), schema=RegisterUser)


def test_login_validate():
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(DOMAIN_URL + LOGIN_API, data=payload)
    validate(instance=response.json(), schema=LoginUser)
