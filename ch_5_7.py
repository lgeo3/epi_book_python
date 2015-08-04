
def exponentiation(x, y):
    """
    This method is in O(y) ... far excessive.. 15 minutes.. me reste 30 minutes pour finir
    encore 10 minutes..
    reste 20 minutes pour finir


    >>> exponentiation(5, 22)
    2384185791015625
    >>> exponentiation(5, -22)
    4.194304e-16
    """
    res = 1
    if x == 1 or y ==0:
        return res

    i = 0

    if y > 0:
        if False:
            pass
        #if y %2  == 0:
        #    a = exponentiation(x, y/2)
        #    return a * a
        else:
            while i != y:
                res *= x
                i += 1
    if y < 0:
        while i != y:
            res = res / float(x)
            i -= 1

    return res




