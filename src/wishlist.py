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
    user = request.args.get('user')

    items = db.query(
        f'SELECT name, price, website, link, rating, img_link FROM wishlist WHERE username = \'{user}\''
    )

    dictionary_items = []
    # loop through db query items to append to dictionary to return
    for item in items:
        dictionary_items.append({"title": item[0], "price": str(item[1]), "website": item[2],
                                 "link": item[3], "rating": str(item[4]), "img_link": item[5]})

    # TODO altered column type of rating and price to real; should we change?

    return jsonify(dictionary_items)

'''
    Adds an item to the user's wishlist
    request body: {"user": <username>, "item":<item info>}
'''
@wishlist_bp.route('/wishlistAdd/', methods=['POST'])
def wishlistAdd():
    data = request.get_json(force=True)
    user = data.get('user')
    item = data.get('item')

    # TODO convert price to generic currency and fix price hack used below

    db.query(
        'INSERT INTO wishlist (username, name, price, website, link, rating, img_link) VALUES(%s, %s, %s, %s, %s, %s, %s)',
        (user, item['title'], item['price'], item['website'], item['link'], item['rating'], item['img_link'])
    )

    return '', 200  # OK


# '''
#     request body: {"user": <username>, "item":<item info>}
# '''
@wishlist_bp.route('/wishlistRemove/', methods=['DELETE'])
def wishlistRemove():
    data = request.get_json(force=True)
    user = data.get('user')
    item = data.get('item')

    db.query(
        'DELETE FROM wishlist WHERE username = %s AND link = %s',
        (user, item['link'])
    )

    return '', 200  # OK


# '''
#     request body: {"user": <username>}
# '''
@wishlist_bp.route('/wishlistClear/', methods=['DELETE'])
def wishlistClear():
    data = request.get_json(force=True)
    user = data.get('user')

    db.query(
        f'DELETE FROM wishlist WHERE username = \'{user}\'',
    )

    return '', 200  # OK
