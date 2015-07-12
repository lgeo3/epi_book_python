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

def hanoi(stacks, labels=[0, 1, 2], n=None, _in=0, _dest=1, _pivot=2):
    """
    Solve hanoi tower problem by recurence (and print the move to be done)

    To represent the peg with int, the higher the number the larger the peg
    We use a list of 3 list to represent each tower

    >>> hanoi([[3, 2, 1], [], []])
    move operation: 0 -> 1
    move operation: 0 -> 2
    move operation: 1 -> 2
    move operation: 0 -> 1
    move operation: 2 -> 0
    move operation: 2 -> 1
    move operation: 0 -> 1
    [[], [3, 2, 1], []]
    """
    if n is None:
        n = len(stacks[_in])
    start_stack = len(stacks[_in]) - n
    p = stacks[_in][start_stack:]
    if len(stacks[_in][start_stack:]) == 1:
        stacks = move_ring(stacks, _in, _dest, labels )
    elif len(stacks[_in]) > 1:
        stacks = hanoi(stacks, labels=labels, n=n-1, _in=_in, _dest=_pivot, _pivot=_dest)
        stacks = move_ring(stacks, _in, _dest, labels)
        stacks = hanoi(stacks, labels=labels, _in=_pivot, _dest=_dest, _pivot=_in, n=n-1)
    return stacks

class NotPermitedMove(Exception):
    pass


def move_ring(stacks, index_in, index_out, labels):
    if len(stacks[index_in]) == 0:
        str = ("NOT PERMITED (no more) move operation:      %s -> %s " % (labels[index_in], labels[index_out]) )
        print(str)
        raise NotPermitedMove(str)
    ring = stacks[index_in][-1]
    if not(len(stacks[index_out])==0 or stacks[index_out][-1] > ring):
        str = ("NOT PERMITED move operation:      %s -> %s " % (labels[index_in], labels[index_out]) )
        print('ring is %s,  stacks[%s][-1] is %s' % (ring, labels[index_out], stacks[index_out][-1]))
        print(str)
        raise NotPermitedMove(str)
    # else: operation is permited
    ring = stacks[index_in].pop(-1)
    stacks[index_out].append(ring)
    print("move operation: %s -> %s " % (labels[index_in], labels[index_out]) )
    return stacks



