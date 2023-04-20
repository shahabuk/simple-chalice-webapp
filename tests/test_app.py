import random
import string

from chalice.test import Client
from app import app


def test_london_is_recognised():
    with Client(app) as client:
        response = client.http.get('/location?place=London')
        actual = response.body.decode("UTF-8")
        assert "London" in actual
        assert "capital" in actual


def test_unknown_is_handled():
    with Client(app) as client:
        unknown_place = random_string()
        response = client.http.get(f'/location?place={unknown_place}')
        actual = response.body.decode("UTF-8")
        assert unknown_place in actual
        assert "Unknown" in actual


def random_string():
    list_of_letters = list(string.ascii_letters)
    random.shuffle(list_of_letters)
    unknown_place = "".join(list_of_letters[:10])
    return unknown_place
