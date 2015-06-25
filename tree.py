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


class BinaryTree(object):
    def __init__(self, data, left=None, right=None):
        if data is None:
            self.isempty = True
            self.data = None
            self.left = None
            self.right = None
        else:
            self.isempty = False
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
        if self.isempty:
            return 0
        return 1 + max(self.left.height(), self.right.height())

##    def __repr__(self):
    ## TO BE DONE
    ## NOT GOOD AT ALL
##        if self.isempty:
##            return "ø"
##        result = " " * self.height() + "%s" % str(self.data)
##        result += "\n"
##        result += self.left.__repr__()
##        result += " " * self.height() * 2
##        result += self.right.__repr__()
##        return result


# TODO: binary tree from list (see Knuth multiple representation of a tree)
## TODO maitriser in order/post order etc..
