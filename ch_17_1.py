

def count_score_combination(W, score):
    """
    Exponential complexity
    :return:

    >>> count_score_combination([], 10)
    0
    >>> count_score_combination([1], 10)
    1
    >>> count_score_combination([1, 2], 3)
    2
    >>> count_score_combination([2, 3, 7], 12)
    4
    """
    count = 0
    if not(W):
        return 0
    if len(W) == 1:
        if score % W[0] == 0:
            return 1
        else:
            return 0

    w0 = W[0]
    k = 0
    while (k * w0) <= score:
        count += count_score_combination(W[1:], score - k*w0)
        k += 1
    return count



# nOW using dynamic programming..
def count_combination(W, score):
    """

    :param W:
    :param score:
    :return:

    >>> count_combination([], 10)
    0
    >>> count_combination([1], 10)
    1
    >>> count_combination([1, 2], 3)
    2
    >>> count_combination([2, 3, 7], 12)
    4

    """
    combination = {i:0 for i in range(score+1)}
    combination[0] = 1
    for w in W:
        for j in range(w, score+1):
            combination[j] += combination[j - w]
    #print(combination)
    return combination[score]

def count_permutation(W, score):
    """
    >>> count_permutation([2, 3, 7], 12)
    20

    """
    permutation = {i:0 for i in range(score+1)}
    permutation[0] = 1
    for i in range(score +1):
        for w in W:
            if i >= w:
                permutation[i] += permutation[i-w]

    print(permutation)
    return permutation[score]

