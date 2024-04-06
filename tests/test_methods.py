import requests
from tests.conftest import DOMAIN_URL, USERS_API

name = 'morpheus'
job = 'leader'
changed_name = 'neo'
changed_job = 'zion resident'
user_id = 2


def test_get_users():
    response = requests.get(DOMAIN_URL + USERS_API, params={'page': 1})
    assert response.status_code == 200
    assert response.json()['page'] == 1
    assert response.json()['per_page'] == 6
    assert response.json()['total'] == 12
    assert response.json()['total_pages'] == 2
    assert len(response.json()['data']) == 6


def test_create_user():
    payload = {
        'name': name,
        'job': job
    }
    response = requests.post(DOMAIN_URL + USERS_API, data=payload)
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'leader'


def test_update_user():
    payload = {
        'name': changed_name,
        'job': changed_job
    }
    response = requests.put(f'{DOMAIN_URL}{USERS_API}/{user_id}', data=payload)
    assert response.status_code == 200
    assert response.json()['name'] == changed_name
    assert response.json()['job'] == changed_job


def test_delete_user():
    response = requests.delete(f'{DOMAIN_URL}{USERS_API}/{user_id}')
    assert response.status_code == 204
    assert response.content == b''


def test_get_single_user_not_found():
    response = requests.get(f'{DOMAIN_URL}{USERS_API}/23')
    assert response.status_code == 404
    assert response.json() == {}
