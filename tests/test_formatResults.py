"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import result_formatter
from bs4 import BeautifulSoup

def test_sortList():
    """
    Checks the sortList function
    """
    arr = [{"title": "Item 2", "price":"$10"}, {"title": "Item 3","price":"$20"}, {"title": "Item 1","price":"$0"}]
    ansArr = [{"title": "Item 1", "price":"$0"}, {"title": "Item 2", "price":"$10"}, {"title": "Item 3", "price":"$20"}]
    revAnsArr = [{"title": "Item 3", "price":"$20"}, {"title": "Item 2", "price":"$10"}, {"title": "Item 1", "price":"$0"}]
    assert result_formatter.sortList(arr, "price", False) == ansArr
    assert result_formatter.sortList(arr, "price", True) == revAnsArr

def test_formatResults():
    """
    Checks the formatResults function
    """
    titles = [BeautifulSoup('<div class="someclass">title  </div>', "html.parser")]
    prices = [BeautifulSoup('<div class="someclass">$0.99  </div>', "html.parser")]
    links = []

    product = result_formatter.formatResult("example", titles, prices, links, "", "")
    ans = {"title":"title", "price":0.99, "website":"example"}
    print(product["website"], ans["website"])

    assert product["title"] == ans["title"] and product["price"] == ans["price"] and product["website"] == ans["website"]
