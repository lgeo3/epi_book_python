# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


## PUTAIN je n'y suis pas arrivé en 15 minutes

def find_maximum_profit(A):
    """
    :param A:
    :return:
    >>> find_maximum_profit([10, 20])
    10
    >>> find_maximum_profit([10, 20, 20, 40])
    30
    >>> find_maximum_profit([20, 10, 20, 40])
    30
    >>> find_maximum_profit([20, 10, 0, 30, 40])
    40
    >>> find_maximum_profit([80, 0, 40])
    40
    >>> find_maximum_profit([0, 80, 10, 40])
    80
    >>> find_maximum_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])
    30

    Complexity is O(n), space complexity n + 2
    """
    cur_profit = 0 # max_profit so far
    buy_index = 0 # corresponding to  min price so far

    for num, val in enumerate(A):
        estimated_profit = val - A[buy_index] # profit if sell today
        if estimated_profit > cur_profit:
            cur_profit = estimated_profit
        elif A[buy_index] > val:
            buy_index = num

    return cur_profit

#TODO: rewrite it using min and max.. not sure to be better.. but ok







