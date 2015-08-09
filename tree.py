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


#TODO: implement drawing propose here : http://billmill.org/pymag-trees/



class BinaryTree(object):
    def __init__(self, data, left=None, right=None):
        if data is None:
            self.is_empty = True
            self.data = None
            self.left = None
            self.right = None
        else:
            self.is_empty = False
            self.data = data
            if left is None:
                left = BinaryTree(None)
            if right is None:
                right = BinaryTree(None)
            self.left = left
            self.right = right

    def height(self):
        """
        just for testing.. not fast
        """
        if self.is_empty:
            return 0
        return 1 + max(self.left.height(), self.right.height())



    def __str__(self):
        if self.is_empty:
            return "NONE"
        else:
            res = [" "] * self.height()/2
            res.append(str(self.data))




def breath_first_search(a_tree):
    #TODO: revoir un print..
    # see for example :  http://stevekrenzel.com/articles/printing-trees
    # print using bfs
    res = []


    to_be_processed = [a_tree]
    current_spaces = a_tree.height() / 2.

    depth = 0
    factor = 1.0
    marker = '8'
    jump = False
    while to_be_processed:
        current_tree = to_be_processed.pop(0)
        if current_tree == '8':
            depth = depth + factor
            if depth %1 == 0 and not(jump):
                print("\n"),
                print('    '* int(A.height() - depth)),
                jump = True
                factor = factor/ 2.
            continue

        #print("depth is %s" % depth)
        print('  ' * int(A.height()-depth//2)),  # TODO .. a revoir..
        if current_tree.is_empty:
            print("."),
            continue

        print("[{}] ".format(current_tree.data)),
        jump = False

        to_be_processed.append(marker)
        to_be_processed.append(current_tree.left)
        to_be_processed.append(current_tree.right)
        to_be_processed.append(marker)




if __name__ == "__main__":
    LeftLeftLeft = BinaryTree(28)
    LeftLeftRight = BinaryTree(0)
    LeftLeft = BinaryTree(271, LeftLeftLeft, LeftLeftRight)
    LeftRightRight = BinaryTree(3)
    LeftRight = BinaryTree(561, None, LeftRightRight)
    RightRight = BinaryTree(271)
    RightLeft = BinaryTree(2)
    Left = BinaryTree(6, LeftLeft, LeftRight)
    Right = BinaryTree(6, RightLeft, RightRight)
    A = BinaryTree(314, Left, Right)

    breath_first_search(A)




























