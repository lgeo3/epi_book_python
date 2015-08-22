




class Node(object):
    __slots__ = 'next', 'data'
    def __init__(self,  data=None):
        self.next = None
        self.data = data

    def __repr__(self):
        return str(self.data)


class LinkList(object):
    def __init__(self):
        self.next = None
        self.data = None
        #self.head.next = None

    def insert_beginning(self, node):
        """
        insert beginning
        :param node:
        :return:
        """
        if type(node) in [float, int]:
            node = Node(node)
        node.next = self.next
        self.next = node

    def pop(self):
        res = self.next
        self.next = self.next.next
        return res

    def __repr__(self):
        cur = self
        res = []
        while cur.next != None:
            res.append(str(cur.next.data))
            cur = cur.next
        return " ----->> ".join(res)


