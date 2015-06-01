# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""

def string_to_int(s):
    """
    >>> string_to_int("123")
    123

    Complexity : O(n) with n length of the string
    """
    tab_conversion = {"0":0, "1":1, "2":2, "3": 3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9}
    val = 0
    lenght = len(s)
    for num, letter in enumerate(s):
        val += tab_conversion[letter] * 10 ** (lenght-num-1)
    return val

def string_to_int_more_efficient(s):
    """
    >>> string_to_int_more_efficient("1")
    1
    >>> string_to_int_more_efficient("108")
    108

    Complexity : O(n) with n length of the string
    """
    tab_conversion = {"0":0, "1":1, "2":2, "3": 3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9}
    val = 0
    sign = 1
    for num, letter in enumerate(s):
        if letter == '-':
            sign = -1
            continue
        val = (val * 10 + tab_conversion[letter])
    val = sign * val
    return val


def int_to_string(val):
    """
    >>> int_to_string(8120830)
    '8120830'
    """
    res = []
    if val < 0 :
        res.append("-")

    while val !=0:
        res.append('%s' % (val % 10))
        val /= 10
    return "".join(reversed(res))



