import json

from flask import Blueprint
from flask import jsonify  # for return
from flask import request  # for url parameter and password

import db

wishlist_bp = Blueprint('wishlist', __name__)

'''
    Get's the user's wishlist
    request body: {"user": <username>}

    return: list of items on wishlist in <item info> schema
'''
@wishlist_bp.route('/wishlist/', methods=['GET'])
def wishlist():
    user = request.form["user"]

    items = db.query(
        f'SELECT name, price, website, link, rating FROM wishlist WHERE username = \'{user}\''
    )

    dictionary_items = []
    # loop through db query items to append to dictionary to return
    for item in items:
        dictionary_items.append({"name": item[0], "price": item[1], "website": item[2],
                                 "link": item[3], "rating": item[4]})

    return jsonify(dictionary_items)


'''
    Adds an item to the user's wishlist
    request body: {"user": <username>, "item":<item info>}
'''
@wishlist_bp.route('/wishlistAdd/', methods=['POST'])
def wishlistAdd():
    user = request.form['user']
    item = request.form['item']

    item = json.loads(item)

    print(item)

    db.query(
        'INSERT INTO wishlist (username, name, price, website, link, rating) VALUES(%s, %s, %s, %s, %s, %s)',
        (user, item['name'], item['price'], item['website'], item['link'], item['rating'])
    )

    return '', 200  # OK


# '''
#     request body: {"user": <username>, "item":<item info>}
# '''
@wishlist_bp.route('/wishlistRemove/', methods=['DELETE'])
def wishlistRemove():
    user = request.form['user']
    item = request.form['item']

    db.query(
        'DELETE FROM wishlist WHERE username = \'%s\' AND name = %s AND price = %s AND'
        'website = %s AND link = %s AND rating = %s',
        (user, item['name'], item['price'], item['website'], item['link'], item['rating'])
    )

    return '', 200  # OK


# '''
#     request body: {"user": <username>}
# '''
@wishlist_bp.route('/wishlistClear/', methods=['DELETE'])
def wishlistClear():
    user = request.form['user']

    db.query(
        f'DELETE FROM wishlist WHERE username = \'{user}\'',
    )

    return '', 200  # OK
