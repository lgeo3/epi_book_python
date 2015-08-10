
def merge_sort_in_place(a, b):
    """



    remark: As there is no native array in python (without numpy for instance) we will use lists to mimick array here.

    :param a: sorted list with empty entry represented by None
    :param b: sorted list
    :return:

    >>> a = [5, 13, 17, None, None, None, None, None]
    >>> b = [3, 7, 11, 19]
    >>> merge_sort_in_place(a, b)
    [3, 5, 7, 11, 13, 17, 19, None]

    """
    #Simple idea fill from the maximum..

    n_filled_in_a = (len(a) - sum([val == None for val in a]))
    insert_index_a = n_filled_in_a + len(b) - 1  # the index to insert the last element of both list in a
    i_a = n_filled_in_a - 1  # the last element of array a
    i_b = len(b) - 1  # the last element of array b

    while insert_index_a >= 0:
        if i_b < 0:
            return  # alredy sorted a
        if i_a < 0:
            a[insert_index_a] = b[i_b]
        elif a[i_a] > b[i_b]:
            a[insert_index_a] = a[i_a]
            i_a = i_a - 1
        else:
            a[insert_index_a] = b[i_b]
            i_b = i_b - 1
        insert_index_a -= 1

    return a



