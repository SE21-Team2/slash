"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""

import result_formatter

def test_formatSearchQuery():
    """
    Checks the formatSearchQuery function
    """
    assert result_formatter.formatSearchQuery("1 2") == "1+2"
    assert result_formatter.formatSearchQuery("A B") == "A+B"
    assert result_formatter.formatSearchQuery("ABC") == "ABC"
