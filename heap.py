""" A binary heap (python implementation)

for a better implem see heaphq

"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
#-----------------------------------------------------------------------------


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue = [item] + self.queue

    def dequeue(self):
        return self.queue.pop(-1)

    def __repr__(self):
        return self.queue

# une heap max
# la structure un tableau:
# ..   b
# p.374  et p.109 Algorithm design manual

class BinaryHeap(object):
    """
    maintains an implicit binary tree structure using an array (i.e a python list)

    the root of tree in first position
    left in second position
    right in third position
    etc..

    left(node_at_position_k) = 2k
    left(node_at_position_k) = 2k+1
    """
    def __init__(self, length=500, object_constructor=None):
        self.items = [None] * length
        self.length = length
        self.last_item_index = 0

    def compare(self, x, y):
        return x>y

    def _left_index(self, item_index):
        res = 1 + 2 * item_index
        if res >= self.last_item_index:
            raise IndexError
        return int(res)

    def _right_index(self, item_index):
        res = 1 + 1 + 2 * item_index
        if res >= self.last_item_index:
            raise IndexError
        return int(res)

    def _parent(self, item_index):
        if item_index == 0:
            return -1
        #return int((item_index - 1) / 2)
        return (item_index - 1) >> 1  # faster using binary operator

    def parent(self, item_index):
        index = self._parent(item_index)
        if index < 0:
            return None
        return self.items[index]

    def _level_order_traversal(self, item_index):
        return self.items[item_index:]

    def _level_order_traversal_old(self, item_index):
        """
        this corresponds to Breadth-first search
        :param item_index:
        :return: two lists current_level, bellow_levels
        """
        q = Queue()
        q.enqueue(item_index)
        res = []
        while True: # queue not empty
            try:
                node_index = q.dequeue()
            except IndexError:
                break
            res.append(node_index)

            for get_child in [self._left_index, self._right_index]:
                try:
                    q.enqueue(get_child(node_index))
                except IndexError:
                    pass
        return res


    def swap(self, index_x, index_y):
        self.items[index_x], self.items[index_y] = self.items[index_y], self.items[index_x]

    def insert(self, value):
        # append to bottom of the tree
        if self.last_item_index + 1 == self.length:
            raise IndexError  # TODO maybe allow a resize ?
        self.items[self.last_item_index] = value

        # check for heap integrity

        item_index = self.last_item_index
        while True:
            if self.parent(item_index) is None:
                break
            if self.compare(self.parent(item_index), value):
                break
            # swap
            self.swap(self._parent(item_index), item_index)
            item_index = self._parent(item_index)

        self.last_item_index += 1

    def extract(self):
        value = self.items[0]
        self.items[0] = None
        self.swap(0, self.last_item_index -1 )
        self.last_item_index  -= 1

        # max heapify
        item_index = 0
        while True:
            largest = item_index

            try:
                left_index = self._left_index(item_index)
                if self.compare(self.items[left_index], self.items[item_index]):
                    largest = left_index
            except IndexError:
                pass

            try:
                right_index = self._right_index(item_index)
                if self.compare(self.items[right_index], self.items[largest]):
                    largest = right_index
            except IndexError:
                pass

            if largest == item_index:
                break
            self.swap(largest, item_index)
            item_index = largest
        return value


    def __repr__(self):
        a = self._level_order_traversal(0)
        return "".join(str(a))




a = BinaryHeap(20)

a.insert(8)
a.insert(15)
a.insert(105)
a.insert(20)
a.insert(3)


for i in range(5):
    print(a.extract())

import heapq

