"""
there is maybee better way to do it in python.. TODO:

for instance :

"""



def spiral_ordering(A):
    """
    Using a recursive call..



    Complexity is O(m) with m the number of element in the matrix.. (we check each item only once)

    TODO : a revoir..

    :param A:
    :return:

    >>> spiral_ordering([[1, 2, 3]])
    [1, 2, 3]

    >>> spiral_ordering([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

    >>> spiral_ordering([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    """

    def _spiral_ordering(A, min_row, max_row, min_column, max_column):
        res = []
        if max_row - min_row == 0:
            return []

        if max_row - min_row == 1:
            return A[min_row][min_column:max_column]

        # up
        for i in range(min_column, max_column-1):
            res.append(A[min_row][i])

        # right column
        for i in range(min_row, max_row-1):
            res.append(A[i][max_column-1])

        # bottom line
        for i in reversed(range(min_column + 1, max_column)):
            res.append(A[max_row-1][i])

        # left column
        for i in reversed(range(min_row + 1, max_row)):
            res.append(A[i][min_column])

        sub_res = _spiral_ordering(A, min_row+1, max_row-1, min_column+1, max_column-1)

        res.extend(sub_res)
        return res

    return _spiral_ordering(A, 0, len(A), 0, len(A[0]))





def spiral_without_recursive_call(A):
    # TODO:

    dx = 1
    dy = 1
    x = 0
    y = 0









