'''
"item info" schema: { "name": ..., "price": ..., "website": ... (amazon, etsy, etc), "link": (url), "rating": ... }
'''

from flask import Blueprint
from flask import jsonify # for return
from flask import request # for url parameter and password

import result_formatter
import scraper

search_bp = Blueprint('search', __name__)

'''
    num_products: number of products to get
    sortby: 'Relevance' or 'Price'
    displayOrder: 'asc' or 'desc'
    currency: currency format

    return: list of items on wishlist in <item info> schema
'''
@search_bp.route('/search/', methods=['GET'])
def search():
    results = scraper.driver(request.args.get('name'), request.args.get('currency'),
                             int(request.args.get('num_products')))

    # if not descending, it is ascending
    results = result_formatter.sortList(results, request.args.get('sortby'),
        request.args.get('displayOrder').lower() == 'desc')

    return jsonify(results)
    