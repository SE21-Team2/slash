"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""
import result_formatter


def test_getCurrency():
    """
    Checks the getNumbers function
    """
    # test valid currency
    assert result_formatter.getCurrency("inr", "$18.99") == 1350
    # test unknown currency
    assert result_formatter.getCurrency("ntd", "$6") == "NTD 0.00"
    # test empty currency
    assert result_formatter.getCurrency("empty", "") == 0.0
