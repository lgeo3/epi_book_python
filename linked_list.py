




class Node(object):
    __slots__ = 'next', 'data'
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    def __repr__(self):
        return str(self.data)


class LinkList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def push(self, node):
        """
        insert beginning
        :param node:
        :return:
        """
        node.next = self.head.next
        self.head.next = node

    def pop(self):
        res = self.head.next
        self.head.next = self.head.next.next
        return res

    def __repr__(self):
        cur = self.head.next
        res = []
        while cur.next != None:
            res.append(str(cur))
            cur = cur.next
        return " ----->> ".join(res)


