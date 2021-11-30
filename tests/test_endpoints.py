# pylint: skip-file
import sys
import os
import pytest

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
import server
from flask import json


@pytest.fixture
def client():
    app = server.create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_search(client) -> None:
    rv = client.get('/search/?name=socks&numProducts=3&sortBy=price&displayOrder=asc')

    # 9 items returned, 3 from each of the 3 implemented sources
    assert len(rv.json) == 3
    # status code check
    assert rv.status_code == 200


def test_user(client) -> None:
    # test signup with an uncommon username
    rv = client.post('/signup/', json={"username": "abcdefg", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid']  # is True
    rv = client.post('/signup/', json={"username": "abcdefg", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert not data['valid']  # is False

    rv = client.post('/login/', json={"username": "abcdefg", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid']  # is True
    rv = client.post('/login/', json={"username": "missing", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert not data['valid']  # is False

    rv = client.delete('/deleteuser/', json={"username": "abcdefg", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid']  # is True
    rv = client.delete('/deleteuser/', json={"username": "abcdefg", "password": "password"})
    data = json.loads(rv.get_data(as_text=True))
    assert not data['valid']  # is False


def test_wishlist(client) -> None:
    try:
        # create 2 test users
        rv = client.post('/signup/', json={"username": "test_user_1", "password": "password"})
        data = json.loads(rv.get_data(as_text=True))
        assert data['valid']  # is True
        rv = client.post('/signup/', json={"username": "test_user_2", "password": "password"})
        data = json.loads(rv.get_data(as_text=True))
        assert data['valid']  # is True

        # nothing in wishlist for both
        rv = client.get('/wishlist/?user=test_user_1')
        assert len(rv.json) == 0
        rv = client.get('/wishlist/?user=test_user_2')
        assert len(rv.json) == 0

        # add one for each
        item = dict(title="socks", price="15.99", website="amazon", link="www.amazon.com/socks", rating=5, img_link="www.amazon.com/socks_image")
        rv = client.post('/wishlistAdd/', json={"user": "test_user_1", "item": item})
        assert rv.status_code == 200  # OK
        item = dict(title="shoes", price="55.99", website="amazon", link="www.amazon.com/shoes", rating=5, img_link="www.amazon.com/shoes_image")
        rv = client.post('/wishlistAdd/', json={"user": "test_user_2", "item": item})
        assert rv.status_code == 200  # no response
        item = dict(title="shirt", price="25.99", website="amazon", link="www.amazon.com/shirt", rating=5, img_link="www.amazon.com/shirt_image")
        rv = client.post('/wishlistAdd/', json={"user": "test_user_2", "item": item})
        assert rv.status_code == 200  # no response

        # get it and verify added items are there
        rv = client.get('/wishlist/?user=test_user_1')
        result = rv.json
        assert len(result) == 1

        expected = {"title": "socks", "price": "15.99", "website": "amazon", "link": "www.amazon.com/socks", "rating": "5", "img_link": "www.amazon.com/socks_image"}
        
        for key in expected:
            if key in result and expected[key] == result[key]:
                assert True
        
        rv = client.get('/wishlist/?user=test_user_2')
        result = rv.json
        assert len(result) == 2
        expected = [
            {"title": "shoes", "price": "55.99", "website": "amazon", "link": "www.amazon.com/shoes", "rating": "5", "img_link": "www.amazon.com/shoes_image"},
            {"title": "shirt", "price": "25.99", "website": "amazon", "link": "www.amazon.com/shirt", "rating": "5", "img_link": "www.amazon.com/shirt_image"}
        ]
        
        for key in expected[0]:
            if key in result[0] and expected[0][key] == result[0][key]:
                assert True
        for key in expected[1]:
            if key in result[1] and expected[1][key] == result[1][key]:
                assert True
        

        item = dict(title="socks", price="15.99", website="amazon", link="www.amazon.com/socks", rating="5", img_link="www.amazon.com/socks_image")
        rv = client.delete('/wishlistRemove/',
                        json={"user": "test_user_1", "item": item})
        assert rv.status_code == 200  # OK
        rv = client.delete('/wishlistClear/', json={"user": "test_user_2"})
        assert rv.status_code == 200  # OK

        # nothing in wishlist for both
        rv = client.get('/wishlist/?user=test_user_1')
        assert len(rv.json) == 0
        assert rv.status_code == 200  # OK

        rv = client.get('/wishlist/?user=test_user_2')
        assert len(rv.json) == 0

        # cleanup test users
        rv = client.delete('/deleteuser/', json={"username": "test_user_1", "password": "password"})
        data = json.loads(rv.get_data(as_text=True))
        assert data['valid']  # is True
        rv = client.delete('/deleteuser/', json={"username": "test_user_2", "password": "password"})
        data = json.loads(rv.get_data(as_text=True))
        assert data['valid']  # is True
    except:
        client.delete('/wishlistClear/', json={"user": "test_user_1"})
        client.delete('/wishlistClear/', json={"user": "test_user_2"})
        client.delete('/deleteuser/', json={"username": "test_user_1", "password": "password"})
        client.delete('/deleteuser/', json={"username": "test_user_2", "password": "password"})
        
        assert False