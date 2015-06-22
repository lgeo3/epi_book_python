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

# debut : 19h48 25 juin 2015
# fin: 20h14 juin 2015
from tree import BinaryTree

def check_bst_property(binary_tree):
    """
    Check if a binary tree satistfies the BST property
    Time Complexity is O(n) we check each node once..
    Space complexity: O(2*height) we use recursive call so we use python stack, so O(2*height if it's a well balanced tree)

    BST property : key stored at a node is greater than or equal to the keys
    stored at it's left subtree and less than or equal to the keys stored in the
    node of it's right subtree.
    """
    # recursive using exception for lazy evaluation
    class BstConditionNotSatisfied(BaseException):
        def __init__(self):
            pass

    def _check_bst_property(binary_tree):
        if binary_tree.isempty:
            return True, None, None
            ##  we could use float('inf') and float('-inf') in place of None to simplifiy thi
            # return True, float('-inf'), float('inf')
        else:
            ## Here we explore left subtree first.. so if the right tree is not BST... close to top
            ## we will still explore all left subtree.. it's sad..
            left_ok, left_min, left_max = _check_bst_property(binary_tree.left)
            right_ok, right_min, right_max = _check_bst_property(binary_tree.right)

            val = binary_tree.data
            level_ok = (left_ok) and (right_ok) and \
            (left_max == None or val >= left_max) and\
            (right_min == None or val <= right_min)

            if not(level_ok):
                raise BstConditionNotSatisfied

            level_min = min([x for x in [val, left_min, right_min] if x is not None])
            level_max = max([x for x in [val, left_max, right_max] if x is not None])

            return level_ok, level_min, level_max

    try:
         result, val_min, val_max = _check_bst_property(binary_tree)
    except BstConditionNotSatisfied:
        return False
    return result


#bst_tree = BinaryTree(19, BinaryTree(7), BinaryTree(43))
#print(check_bst_property(bst_tree))
#
#not_bst_tree = BinaryTree(44, BinaryTree(7), BinaryTree(43))
#print(check_bst_property(not_bst_tree))
#

# As suggested in the book :

