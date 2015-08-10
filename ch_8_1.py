from linked_list import LinkList, Node

def merge_two_sorted_linked_list(L, F):
    """

    :param L:
    :param F:
    :return:

    >>> L = LinkList()
    >>> L.insert_beginning(7)
    >>> L.insert_beginning(5)
    >>> L.insert_beginning(2)
    >>> F = LinkList()
    >>> F.insert_beginning(11)
    >>> F.insert_beginning(3)
    >>> merge_two_sorted_linked_list(L, F)
    2 ----->> 3 ----->> 5 ----->> 7 ----->> 11
    """
    M = LinkList()
    a = M
    cur_node_in_M = M

    while F.next != None or L.next != None:
        if F.next == None:
            cur_node_in_M.next = L.pop()
            return M
        elif L.next == None:
            cur_node_in_M.next = F.pop()
            return M

        if L.next.data <= F.next.data:
            cur_node_in_M.next = L.pop()
        else:
            cur_node_in_M.next = F.pop()

        cur_node_in_M = cur_node_in_M.next


    return M
