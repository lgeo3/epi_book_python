import itertools

# il me reste 30 minutes.


def not_in_conflict(new_queen, other_queens):

    # check line
    if new_queen[0] in [queen[0] for queen in other_queens]:
        return False


    # ckeck column
    if new_queen[1] in [queen[1] for queen in other_queens]:
        return False

    # check diagonal
        ## TODO a finir
    #if [[new_queen[0]+dx, new_queen[1]+dy] in other_queens  for dx in range()
    #    return False


def all_non_attacking_queens(n):
    """

    :param n:
    :return:
    """


    def _non_attacking_queen(grid_size, current_queens=[], n):
        if n == 0:
            res = []

        if n == 1:
            if current_queens is []:
                for new_queen in (itertools.permutations(range(grid_size), 2)):
                    if not_in_conflict(new_queen, current_queens):
                        configuration = current_queens + [new_queen]
                        res.append(configuration)


        else:

            for current_queens in itertools.permutations(range(grid_size), 2):
                sub_res =  _non_attacking_queen(grid_size, current_queens, n-1)
                if sub_res != []:
                    res.extend(sub_res)

        return res


