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


def bsearch_brute_force(sorted_int_list, q_val):
    """
    Search a val in a list (bruteforce version complexity: O(n))

    return index of first occurence of `q_val` in sorted_int_list
    return None if not found
    >>> A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    >>> bsearch_brute_force(A, 108)
    3
    >>> bsearch_brute_force(A, 285)
    6
    >>> bsearch_brute_force(A, 823913)

    """
    for index, val in enumerate(sorted_int_list):
        if val == q_val:
            return index


def bsearch(sorted_int_list, q_val):
    """
    Search a val in a list (complexity: ???)

    return index of first occurence of `q_val` in sorted_int_list
    return None if not found
    >>> A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    >>> bsearch(A, 108)
    3
    >>> bsearch(A, 285)
    6
    >>> bsearch(A, 823913)
    """
    # l'idee c'est de decouper la liste.. on part au milieu
    A = sorted_int_list
    left = 0
    right = len(A)
    index = 0
    while True:
        if left >= len(A):
            #print("left {} > right {}".format(left, right))
            #raise(IndexError)
            return None
        index = left + int( (right - left) / 2)
        if A[index] < q_val:
            left = index + 1
            continue
        if A[index] > q_val:
            right = index - 1
            continue
        if A[index] == q_val:
            break

    #A[index] == q_val
    ## now searching for first occurence if multiple
    left = left
    right = index
    while right-left >= 1:
        index = left + int( (right - left) /2 )
        if A[index] == q_val:
            right = index
            continue
        if A[index] != q_val:
            left = index
            continue
    return right
