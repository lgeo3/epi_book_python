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

# structure: un disque = un entier, avec 0 le plus gros de tous
# 3 stack represente par des listes python (append et pop(-1))

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
    print("move operation:      %s -> %s " % (labels[index_in], labels[index_out]) )
    return stacks


def hanoi(stacks, labels=[0, 1, 2], start_stack=0, _in=0, _dest=1, _pivot=2):
    print("hanoi")
    if len(stacks[_in][start_stack:]) == 1:
        stacks = move_ring(stacks, _in, _dest, labels )
    elif len(stacks[_in]) > 1:
        stacks = hanoi(stacks, labels=labels, start_stack=start_stack+1, _in=_in, _dest=_pivot, _pivot=_dest)
        stacks = move_ring(stacks, _in, _dest, labels)
        stacks = hanoi(stacks, labels=labels, _in=_pivot, _dest=_dest, _pivot=_in)

    return stacks
# ca ne marche pas pour [5,4,3,2] .. et merde..


#def hanoi(stack_1, stack_2 = [], stack_3 = [], n=None, label='123'):
#    """
#    >>> hanoi([1,2,3,4,5])
#    [], [], [1,2,3,4,5]
#
#    This function move Stack 1 to stack 3
#    """
#    if n is None:
#        n = len(stack_1)
#    start_index = len(stack_1)-n
#    sub_stack = stack_1[start_index:]
#    if len(sub_stack) == 0:
#        pass # ??
#    elif len(sub_stack) == 1:
#        val = sub_stack.pop(-1)
#        stack_3.append(val)
#        # we also remove it from the stack1
#        stack_1 = stack_1[0:start_index] + sub_stack
#    else:
#        stack_1, stack_2, stack_3 = hanoi(stack_1, stack_2, stack_3, n-1)
#        val = stack_1.pop(-1)
#        stack_2.append(val)
#        print("BEFORE RECOURSION")
#        print(locals())
#
#        print("CALLING hanoi to move all stack3 above current stack_2")
#        stack_3, stack_1, stack_2 = hanoi(stack_3, stack_1, stack_2, len(stack_3), label='312')
#        print("CALLING hanoi to move all stack2 to stack_3")
#        stack_2, stack_1, stack_3 = hanoi(stack_2, stack_1, stack_3, len(stack_2), label='213')
#
#    print("%s: %s:" % (label, locals()))
#    return stack_1, stack_2, stack_3
#
##assert((hanoi([1]))==([],[],[1]))
##assert(hanoi([1,2])==([],[1,2], []))
##print(hanoi([1, 2]))
##print(hanoi([1,2,3,4,5]))


def autotest():
    assert((hanoi([1]))==([],[],[1]))
    assert(hanoi([1,2])==([],[1,2], []))

#autotest()
