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
    Gets details of items from e-commerce websites specified by the query parameters.
    request body: 
        name: search product string
        numProducts: number of products to get
        sortBy: 'Relevance' or 'Price'
        displayOrder: 'asc' or 'desc'
        currency: currency format

    return: list of items on wishlist in <item info> schema
'''
@search_bp.route('/search/', methods=['GET'])
def search():
    results = scraper.driver(request.args.get('name'), request.args.get('numProducts', type=int))

    # if not descending, it is ascending
    results = result_formatter.sortList(results, request.args.get('sortBy'),
        request.args.get('displayOrder').lower() == 'desc')

    return jsonify(results)
