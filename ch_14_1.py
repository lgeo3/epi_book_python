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

# debut : 16h54, 22 juin 2015
# fin : 17h29, 22 juin 2015


def easy_intersection(A, B):
    """
    of course using python set it's easy to do the exercise
    >>> set([5,6,8]) == easy_intersection([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10])
    True
    """
    return (set(A).intersection(set(B)))


def intersection(A, B):
    """
    compute the intersection of two sorted arrays

    Time complexity is O(n+m) with n, m lengh of respectively A and B
    Space complexity is O(1)

    This solution is good if the two array have similar size

    >>> intersection([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10])
    [5, 6, 8]

    >>> intersection([2,3,3,5,5,6,7,7,8,12], [])
    []
    """
    result = []
    if len(A) == 0 or len(B) == 0:
        return result

    indexes = [0, 0]  # for A and B
    last_append_value = None
    while True:
        try:
            if A[indexes[0]] == B[indexes[1]]:
                if last_append_value != A[indexes[0]]:
                    result.append(A[indexes[0]])
                    last_append_value = A[indexes[0]]
                indexes[0] += 1
                indexes[1] += 1
                continue
            elif A[indexes[0]] < B[indexes[1]]:
                indexes[0] += 1
                continue
            else:
                indexes[1] += 1
                continue
        except IndexError:
            break  # we quit the loop, one array reach end
    return result

def intersection_different_size(A,B):
    """
    use this one if one array is really bigger than the second one

    Here we suppose that len(A) >>>> len(B)


    >>> intersection_different_size([2,3,3,5,5,6,7,7,8,12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,], [5,5,6,8,8,9,10,10])
    [5, 6, 8]
    """
    from ch_12_1 import bsearch
    result = []
    last_append_value = None
    for val in B:
        if val  == last_append_value:
            continue
        if bsearch(A, val):
            result.append(val)
            last_append_value = val
    return result

