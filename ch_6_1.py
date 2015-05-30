""" A one-line description.

A longer description that spans multiple lines.  Explain the purpose of the
file and provide a short list of the key classes/functions it contains.  This
is the docstring shown when some does 'import foo;foo?' in IPython, so it
should be reasonably useful and informative.
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

def dutch_flag_partion_using_temporary_list(A, pivot_index=0):
    """
    Brute force version

    :param A: an array
    :param pivot_index:
    :return: reaarrange value of A with all values < A[pivot_index] first, then values == A[pivot_index] then values > A[pivot_index]
    >>> A = [10, 8, 3, 20, 3, 8, 1]
    >>> dutch_flag_partion_using_temporary_list(A, 2)
    [1, 3, 3, 10, 8, 20, 8]
    """
    n = len(A)
    left = []
    mid = []
    right = []

    for index, val in enumerate(A):
        if val < A[pivot_index]:
            left.append(val)
        elif val == A[pivot_index]:
            mid.append(val)
        else:
            right.append(val)

    return left + mid + right

# Complexity:
# time complexity : O(n) with n the length of A
# space complexity: O(2n)


# on veut une version inplace

## TODO: etre capable de le refaire rapidement
def dutch_flag_partition(A, pivot_index=0):
    """
    >>> A = [10, 8, 3, 20, 3, 8, 1]
    >>> dutch_flag_partition(A, 2)
    [1, 3, 3, 20, 8, 8, 10]
    """
    n = len(A)

    smaller = 0
    equal = 0
    bigger = n-1
    # unclassified = [equal:larger]

    val_pivot = A[pivot_index]

    while equal <= bigger:
        val = A[equal]
        if val < val_pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif val == val_pivot:
            equal +=1
            # no move
        else:  #elif val > val_pivot:
            A[bigger], A[equal] = A[equal], A[bigger]
            bigger -= 1

    return A





