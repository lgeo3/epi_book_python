__author__ = 'seto'

def _construct_adjacency_matrix(people=10, celebrity=8):
    import random
    random.seed(0)   # for reproductible matrix
    matrix = []
    for user in range(people):
        if user == celebrity:
            current_line = [False] * people
        else:
            current_line = [random.choice([True, False]) for x in range(people)]
            current_line[user] = False
            current_line[celebrity] = True
        matrix.append(current_line)
    return matrix


def identify_the_celebrity(adjacency_matrix):
    """
    Complexity is O(n)

    :param adjacency_matrix:
    :return:

    >>> identify_the_celebrity(_construct_adjacency_matrix(1000, 835))
    835
    """
    n_users = len(adjacency_matrix)
    i = 0
    j = 1

    while j < n_users:
        if adjacency_matrix[i][j]:
            i = j
        j = j + 1
    return i


