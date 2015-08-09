import itertools

# il me reste 30 minutes.


def diag_a(x, y, n):
    res = []
    res.extend([(x-i,y-i) for i in range(0, n)])
    res.extend([(x+i,y+i) for i in range(0, n)])

    res = [(i,j) for (i,j) in res if (i in range(0,n)) and (j in range(0,n))]
    return set(res)


def diag_b(x, y, n):
    res = []
    res.extend([(x-i,y+i) for i in range(0, n)])
    res.extend([(x+i,y-i) for i in range(0, n)])

    res = [(i,j) for (i,j) in res if (i in range(0,n)) and (j in range(0,n))]
    return set(res)

def not_in_conflict(new_queen, other_queens, n):

    # check line
    if new_queen[0] in [queen[0] for queen in other_queens]:
        #print("Line")
        return False

    # ckeck column
    if new_queen[1] in [queen[1] for queen in other_queens]:
        #print("Columnd")
        return False

    # check diagonal
    ## TODO a finir
    c = [diag_queen in other_queens for diag_queen in diag_b(new_queen[0], new_queen[1], n)]
    if True in c:
        #print('diag_b')
        return False

    c =  [diag_queen in other_queens  for diag_queen in diag_a(new_queen[0], new_queen[1], n)]
    if True in c:
        #print('diag_a')
        return False

    return True


def all_non_attacking_queens(n):
    """

    :param n:
    :return:
    """
    final_res = set()


    def _non_attacking_queen(grid_size, current_queens=None, n=1):
        if current_queens is None:
            current_queens = []

        res = []
        if n == 0:
            res = current_queens
        #    print("Curr %s" % str(current_queens))
            # we need to add it to the main..
            final_res.add(frozenset(current_queens))
        else:
            for new_queen in (itertools.product(range(grid_size), repeat=2)):
                new_queen = tuple(new_queen)
                #print('testing new_queen {}'.format(new_queen))
                if not_in_conflict(new_queen, current_queens, grid_size):
                    c = current_queens + [new_queen]
                    sub_res = _non_attacking_queen(grid_size, current_queens=c, n=n-1)
                    #print("SUB res {}".format( sub_res))
                    if sub_res:
        #                print("OK {} appending to res {} ".format(sub_res, res))
                        res.append(sub_res)
        #                print('new res is now %s' % res)
        #print("Return is %s" % str(res))
        return res

    _non_attacking_queen(n, None, n)
    return final_res

def test_ok():
    assert(len(all_non_attacking_queens(1)) == 1)
    assert(len(all_non_attacking_queens(2)) == 0)
    assert(len(all_non_attacking_queens(3)) == 0)
    assert(len(all_non_attacking_queens(4)) == 2)
    assert(len(all_non_attacking_queens(5)) == 10)
    assert(len(all_non_attacking_queens(6)) == 4)
    assert(len(all_non_attacking_queens(7)) == 40)

def test():

    import pylab
    a = (all_non_attacking_queens(5))
    import numpy as np
    for configuration in a:
        print("configuration %s" % configuration)
        tab = np.zeros((5,5))
        for coord in configuration:
            print("coord {}".format(coord))
            tab[coord[0], coord[1]] = 1

        pylab.imshow(tab, interpolation='None', cmap='binary')
        pylab.grid(True)
        pylab.show()


    print("'iii'")
    print(a)


test_ok()
#test()
