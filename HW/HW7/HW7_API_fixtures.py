import pytest
import requests
from pprint import pprint

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200


@pytest.fixture(scope='function')
def booking_id():
    payload = {
        "firstname": "Bob",
        "lastname": "Jimmisson",
        "totalprice": 659,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-20",
            "checkout": "2023-10-27"
        },
        "additionalneeds": "Seaside"}
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    # в фикстурах принято использовать yield вместо return
    yield booking_id


@pytest.fixture(scope='module')
def token():
    payload = {
    "username" : "admin",
    "password" : "password123"}
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


def test_update_booking(booking_id, token):
    header = {'Cookie': f'token={token}'}
    payload = {
        "firstname": "Iggy",
        "lastname": "Hendrix",
        "totalprice": 666,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-20",
            "checkout": "2023-10-27"
        },
        "additionalneeds": "Seaside"}
    response = requests.put(f'{BASE_URL}/{booking_id}', headers=header, json=payload)
    assert response.status_code == STATUS_OK


def test_partial_update_booking(booking_id, token):
    header = {'Cookie': f'token={token}'}
    payload = {
        "firstname": "Ozzy",
        "lastname": "Malmsten"}
    response = requests.patch(f'{BASE_URL}/{booking_id}', headers=header, json=payload)
    assert response.status_code == 200



