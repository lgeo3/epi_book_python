# SUDOKU

def sudoku_checker(grid):
    """
    TODO: complexity analysis O(n^2)
    :param grid:
    :return:

    >>> grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],\
    [6, 0, 0, 1, 9, 5, 0, 0, 0],\
    [0, 9, 8, 0, 0, 0, 0, 6, 0],\
    [8, 0, 0, 0, 6, 0, 0, 0, 3],\
    [4, 0, 0, 8, 0, 3, 0, 0, 1],\
    [7, 0, 0, 0, 2, 0, 0, 0, 6],\
    [0, 6, 0, 0, 0, 0, 2, 8, 0],\
    [0, 0, 0, 4, 1, 9, 0, 0, 5],\
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    >>> sudoku_checker(grid)
    True

    >>> grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],\
    [6, 0, 0, 1, 9, 5, 0, 0, 0],\
    [0, 9, 8, 0, 0, 0, 0, 6, 0],\
    [8, 0, 0, 0, 6, 0, 0, 0, 3],\
    [4, 0, 8, 8, 0, 3, 0, 0, 1],\
    [7, 0, 0, 0, 2, 0, 0, 0, 6],\
    [0, 6, 0, 0, 0, 0, 2, 8, 0],\
    [0, 0, 0, 4, 1, 9, 0, 0, 5],\
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    >>> sudoku_checker(grid)
    row 4 failed
    False

    >>> grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],\
    [6, 0, 0, 1, 9, 5, 0, 0, 0],\
    [0, 9, 8, 0, 0, 0, 0, 6, 0],\
    [8, 0, 0, 0, 6, 0, 0, 0, 3],\
    [4, 0, 0, 8, 0, 3, 0, 0, 1],\
    [7, 0, 8, 0, 2, 0, 0, 0, 6],\
    [0, 6, 0, 0, 0, 0, 2, 8, 0],\
    [0, 0, 0, 4, 1, 9, 0, 0, 5],\
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    >>> sudoku_checker(grid)
    column 2 failed
    False

    >>> grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],\
    [6, 0, 0, 1, 9, 5, 0, 0, 0],\
    [0, 9, 8, 0, 0, 0, 0, 6, 0],\
    [8, 0, 0, 0, 6, 0, 0, 0, 3],\
    [4, 0, 0, 8, 0, 3, 0, 0, 1],\
    [7, 0, 0, 0, 2, 0, 0, 0, 6],\
    [0, 6, 0, 0, 0, 0, 2, 8, 0],\
    [0, 0, 0, 4, 1, 9, 0, 0, 5],\
    [0, 0, 0, 0, 8, 0, 5, 7, 9]]
    >>> sudoku_checker(grid)
    Subgrid 8 failed
    False

    """
    def check(a):
        """
        check uniqueness of each number ..
        :param a:
        :return: True if a number is present only one (except for 0 that can be here multiple time)
        """
        current_set = set()
        for val in a:
            if val != 0:
                if val in current_set:
                    return False
            current_set.add(val)
        return True

    def _get_sub_grids(grid, width=3, height=3):
        start_x, start_y = 0, 0
        dx = 1
        dy = 0
        for dx in [0, 1, 2]:
            for dy in [0, 1, 2]:
                start_x = width * dx
                start_y = height * dy

                res = [grid[start_x+i][start_y+j] for i in range(width) for j in range(height)]
                yield res

    for row in range(0, len(grid)-1):
        if check(grid[row]) is False:
            print("row %s failed" % row)
            return False

    for column in range(0, len(grid[0]) -1):
        if check([grid[i][column] for i in range(len(grid)-1)]) is False:
            print("column %s failed" % column)
            return False

    for num, sub_grid in enumerate(_get_sub_grids(grid)):
        if check(sub_grid) is False:
            print("Subgrid %s failed" % num)
            return False
    return True


