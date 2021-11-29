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
    sortBy = request.args.get('sortBy')
    numProducts = request.args.get('numProducts', type=int)

    results = scraper.driver(request.args.get('name'), request.args.get('numProducts', type=int))

    # if not descending, it is ascending
    results = result_formatter.sortList(results, sortBy,
        request.args.get('displayOrder').lower() == 'desc')

    if sortBy == "relevance":
        walmart_results = list(filter(lambda x: x["website"] == "walmart", results))
        etsy_results = list(filter(lambda x: x["website"] == "Etsy", results))
        amazon_results = list(filter(lambda x: x["website"] == "amazon", results))

        total = len(walmart_results) + len(etsy_results) + len(amazon_results)
        numToPop = total - numProducts


        while numToPop > 0:
            if len(walmart_results) > len(etsy_results) and len(walmart_results) > len(amazon_results):
                walmart_results.pop()
            elif len(etsy_results) > len(amazon_results):
                etsy_results.pop()
            else:
                amazon_results.pop()
            numToPop -= 1

        results = walmart_results + etsy_results + amazon_results
    elif sortBy == "price" or sortBy == "rating":
        results = results[:min(numProducts, len(results))]


    return jsonify(results)
