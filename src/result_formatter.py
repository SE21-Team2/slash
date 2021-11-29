"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com
The formatter module focuses on processing raw text and returning it in
the required format.
"""

import math
from datetime import datetime


def formatResult(website, titles, prices, links, ratings):
    """
    The formatResult function takes the scraped HTML as input, and extracts the
    necessary values from the HTML code. Ex. extracting a price '$19.99' from
    a paragraph tag.
    Parameters: website- name of the website where the result is from
                titles- scraped titles of the products,
                prices- scraped prices of the products,
                links- scraped links of the products on the respective e-commerce sites,
                ratings-scraped ratings of the product,
                currency- currency type entered by the user
    Returns: A dictionary of all the parameters stated above for the product
    """

    title, price, link, rating = '', '', '', ''
    if titles:
        title = titles[0].get_text().strip()
    if prices:
        price = ''.join(c for c in prices[0].get_text().strip() if c in '0123456789.')
    # if '$' not in price:
    #     price = '$'+price
    price = price.replace('$', '')
    price = float('0' if price == '' else price)
    if links:
        link = links[0]['href']
    formatted_link = link if 'https://' in link else f'https://www.{website}.com{link}'
    if ratings:
        rating = float(ratings[0].get_text().strip().split()[0])
    product = {
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "title": title,
        "price": price,
        "link": formatted_link,
        "website": website,
        "rating": rating
    }

    return product


def sortList(arr, sort_by, reverse):
    """ It sorts the products list based on the flags provided as arguments.
        Currently, it supports sorting by price.
        Parameters- SortBy- "pr": sorts by price, "ra": sorts by rating
        Returns- Sorted list of the products based on the parameter requested by the user
    """
    if sort_by == "pr":
        return sorted(arr, key=lambda x: getNumbers(x["price"]), reverse=reverse)
    if sort_by == "ra":
        return sorted(arr, key=lambda x: getNumbers(x["rating"]), reverse=reverse)
    return arr


def formatSearchQuery(query):
    """ It formats the search string into a string that can be sent as a url paramenter.
    """
    return query.replace(" ", "+")


# def formatTitle(title):
#     """ It formats titles extracted from the scraped HTML code.
#     """
#     title = title.strip()
#     if len(title) > 40:
#         return title[:40] + "..."
#     return title


def getNumbers(st):
    """ It extracts float values for the price from a string.
    Ex. it extracts 10.99 from '$10.99' or 'starting at $10.99'
    """
    ans = ''
    for ch in st:
        if ('0' <= ch <= '9') or ch == '.':
            ans += ch
    try:
        ans = float(ans)
    except ValueError:
        ans = math.inf
    return ans


# def getCurrency(currency, price):
#     """
#     The getCurrency function converts the prices listed in USD to user specified currency.
#     Currently it supports INR, EURO, AUD, YUAN, YEN, POUND
#     """

#     converted_cur = 0.0
#     if len(price) > 1:
#         if currency == "inr":
#             converted_cur = 75 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         elif currency == "euro":
#             converted_cur = 1.16 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         elif currency == "aud":
#             converted_cur = 1.34 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         elif currency == "yuan":
#             converted_cur = 6.40 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         elif currency == "yen":
#             converted_cur = 114.21 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         elif currency == "pound":
#             converted_cur = 0.74 * int(price[(price.index("$")+1):price.index(".")].replace(",", ""))
#         converted_cur = currency.upper()+' '+str(converted_cur)
#     return converted_cur
