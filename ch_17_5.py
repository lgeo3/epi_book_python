

def search_for_sequence(S, A):
    """
    WARNING it does works only if number in A are unique, if there are multiple path in A (i.e same number multiple time) this does not work.

    :param S:
    :param A:
    :return:

    ok for complexity:
    building neighbors table = O(n*m*4)
    then looping over S = O(len(S))  # we have O(1) access because we use dictionary

    so final complexity is O(n*m) with n number of row, m number of column in matrix

    >>> A = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    >>> S = [1, 3, 4, 6]
    >>> search_for_sequence(S, A)
    [(0, 0), (1, 0), (1, 1), (2, 1)]
    """
    def _neighbors(A, row=0, col=0):
        max_row = len(A)
        max_col = len(A[0])
        res = dict()
        for shift in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row = row + shift[0]
            new_col = col + shift[1]
            if  (0 <= new_col < max_col) and (0 <= new_row < max_row):
                res[A[new_row][new_col]] = (new_row, new_col)
        return res

    neighbors = dict()
    first_coordinate = None
    for row in range(len(A)):
        for col in range(len(A[0])):
            val = A[row][col]
            if val == S[0]:
                first_coordinate  = (row, col)
            neighbors[val] = _neighbors(A, row, col)

    if first_coordinate is None:
        return False

    res = [first_coordinate]

    for num, val in enumerate(S[:-1]):
        if S[num+1] in neighbors[val]:
            coordinate = neighbors[val][S[num+1]]
            res.append(coordinate)
        else:
            return False
    return res















































