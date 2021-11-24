'''
"item info" schema: { "name": ..., "price": ..., "website": ... (amazon, etsy, etc), "link": (url), "rating": ... }
'''

from flask import Blueprint
from flask import jsonify # for return
from flask import request # for url parameter and password

wishlist_bp = Blueprint('wishlist', __name__)

'''
    request body: {"user": <username>}

    return: list of items on wishlist in <item info> schema
'''
@wishlist_bp.route('/wishlist/', methods=['GET'])
def wishlist():
    user = request.form["user"]
    '''
    items = db.query(
        'SELECT name, price, website, link, rating FROM wishlist WHERE username = %s',
        (user)
    )

    for item in items:
        item = { "name":item[0], "price":price, "website":website, "link":link, "rating":rating }
    
    # how does jsonify look with db return, this is single item
    return jsonify(items)
    '''

    # return a default JSON message
    return jsonify(
        [
            {
            "name":"test_name",
            "price":"$0.00",
            "website":"Google",
            "link":"www.google.com",
            "rating":5
            },
            {
            "name":"test_name2",
            "price":"$0.00",
            "website":"Amazon",
            "link":"www.amazon.com",
            "rating":5
            }
        ]
    )

'''
    request body: {"user": <username>, "item":<item info>}
'''
@wishlist_bp.route('/wishlistAdd/', methods=['POST'])
def wishlistAdd():
    user = request.form['user']
    item = request.form['item']

    '''
    db.query(
            'INSERT INTO wishlist (username, name, price, website, link, rating) VALUES(%s, %s, %s, %s, %s, %s)',
            (user, item[0], item[1], item[2], item[3], item[4], item[5])
    )
    '''

    return ('', 204) # no content

'''
    request body: {"user": <username>, "item":<item info>}
'''
@wishlist_bp.route('/wishlistRemove/', methods=['POST'])
def wishlistRemove():
    user = request.form['user']
    item = request.form['item']

    '''
    db.query(
            'DELETE FROM wishlist WHERE username = %s AND name = %s AND price = %s AND website = %s AND link = %s AND rating = %s',
            (user, item[0], item[1], item[2], item[3], item[4], item[5])
    )
    '''

    return ('', 204) # no content