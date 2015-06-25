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

def hanoi(stack_1, stack_2 = [], stack_3 = [], n=None, label='123'):
    """
    >>> hanoi([1,2,3,4,5])
    [], [], [1,2,3,4,5]

    move stack1 to stack3
    """
    if n is None:
        n = len(stack_1)
    start_index = len(stack_1)-n
    sub_stack = stack_1[start_index:]
    if len(sub_stack) == 0:
        pass
    elif len(sub_stack) == 1:
        val = sub_stack.pop(-1)
        stack_3.append(val)
        # we also remove it from the stack1
        stack_1 = stack_1[0:start_index] + sub_stack
    else:
        stack_1, stack_2, stack_3 = hanoi(stack_1, stack_2, stack_3, n-1)
        val = stack_1.pop(-1)
        stack_2.append(val)
        print("BEFORE RECOURSION")
        print(locals())

        print("CALLING hanoi to move all stack3 above current stack_2")
        stack_3, stack_1, stack_2 = hanoi(stack_3, stack_1, stack_2, len(stack_3), label='312')
        print("CALLING hanoi to move all stack2 to stack_3")
        stack_2, stack_1, stack_3 = hanoi(stack_2, stack_1, stack_3, len(stack_2), label='213')

    print("%s: %s:" % (label, locals()))
    return stack_1, stack_2, stack_3

#assert((hanoi([1]))==([],[],[1]))
#assert(hanoi([1,2])==([],[1,2], []))
print(hanoi([1, 2]))
#print(hanoi([1,2,3,4,5]))
