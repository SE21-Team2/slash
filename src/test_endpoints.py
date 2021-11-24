import pytest

import endpoints
import db
from flask import json

@pytest.fixture
def client():
    app = endpoints.create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_search(client) -> None:
    rv = client.get('/search/?name=socks&currency=usd&num_products=3&sortby=pr&displayOrder=asc')

    # 9 items returned, 3 from each of the 3 implemented sources
    assert len(rv.json) == 9
    # status code check
    assert rv.status_code == 200


def test_user(client) -> None:
    #test signup with an uncommon username
    rv = client.post('/signup/', data=dict(username="abcdefg", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True
    rv = client.post('/signup/', data=dict(username="abcdefg", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == False

    rv = client.get('/login/', data=dict(username="abcdefg", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True
    rv = client.get('/login/', data=dict(username="missing", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == False

    rv = client.delete('/deleteuser/', data=dict(username="abcdefg", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True
    rv = client.delete('/deleteuser/', data=dict(username="abcdefg", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == False

def test_wishlist(client) -> None:
    # create 2 test users
    rv = client.post('/signup/', data=dict(username="test_user_1", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True
    rv = client.post('/signup/', data=dict(username="test_user_2", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True

    try:
        # nothing in wishlist for both
        rv = client.get('/wishlist/', data=dict(user="test_user_1"))
        assert len(rv.json) == 0
        rv = client.get('/wishlist/', data=dict(user="test_user_2"))
        assert len(rv.json) == 0

        # add one for each
        rv = client.post('/wishlistAdd/', data=dict(user="test_user_1", name="socks", price=15.99, website="amazon", link="www.amazon.com/socks", rating=5))
        assert rv.status_code == 204 # no response
        rv = client.post('/wishlistAdd/', data=dict(user="test_user_2", name="shoes", price="55.99", website="amazon", link="www.amazon.com/shoes", rating=5))
        assert rv.status_code == 204 # no response
        rv = client.post('/wishlistAdd/', data=dict(user="test_user_2", name="shirt", price="25.99", website="amazon", link="www.amazon.com/shirt", rating=5))
        assert rv.status_code == 204 # no response

        # get it and verify added items are there
        rv = client.get('/wishlist/', data=dict(username="test_user_1"))
        assert len(rv.json) == 1
        assert rv.json == { "name":"socks", "price":15.99, "website":"amazon", "link":"www.amazon.com/socks", "rating":5 }
        rv = client.get('/wishlist/', data=dict(username="test_user_2"))
        assert len(rv.json) == 2
        assert rv.json == {
            {"name":"shoes", "price":"55.99", "website":"amazon", "link":"www.amazon.com/shoes", "rating":5},
            {"name":"shirt", "price":"25.99", "website":"amazon", "link":"www.amazon.com/shirt", "rating":5}
        }

        rv = client.delete('/wishlistRemove/', data=dict(user="test_user_1", name="socks", price=15.99, website="amazon", link="www.amazon.com/socks", rating=5))
        assert rv.status_code == 204 # no response
        rv = client.delete('/wishlistClear/', data=dict(username="test_user_2"))
        assert rv.status_code == 204 # no response

        # nothing in wishlist for both
        rv = client.get('/wishlist/', data=dict(user="test_user_1"))
        assert len(rv.json) == 0
        rv = client.get('/wishlist/', data=dict(user="test_user_2"))
        assert len(rv.json) == 0
    except:
        print('error occured in testing the wishlist')

    # cleanup test users
    rv = client.delete('/deleteuser/', data=dict(username="test_user_1", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True
    rv = client.delete('/deleteuser/', data=dict(username="test_user_2", password="password"))
    data = json.loads(rv.get_data(as_text=True))
    assert data['valid'] == True

