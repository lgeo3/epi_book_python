import random
import pylab

def old_sample_offline_data(A, k):

    """
    a try without recursion and only two call to random number generator.. :D
    :param A:
    :param k:
    :return:

    """
    #sample_offline_data([1,2,3], 1)
    if k == 0:
        return []

    if k == len(A):
        return A

    N = len(A)
    start = random.randint(0, N-1)
    step = random.randint(1, (N+1)//k)

    res = []
    cur_pos = start
    while len(res) < k:
        res.append(A[cur_pos])
        cur_pos = (cur_pos + step) % N
    return res

def sample_offline_data_rec(A, k):
    """
    version as in the book solution
    :param A:
    :param k:
    :return:
    """
    if k == 0:
        return []
    if k == 1:
        return [A[random.randint(0, len(A)-1)]]

    index = random.randint(0, len(A)-1)
    A[-1], A[index] = A[index], A[-1] # swapping with python is easy
    return [A[-1]] + sample_offline_data_rec(A[0:-1], k-1)

def sample_offline_data_numpy(A, k):
    import numpy
    return numpy.random.choice(A,k, replace=False)

# numpy code use swap thing.. and rk_interval for shuffling the code is here : https://github.com/numpy/numpy/blob/master/numpy/random/mtrand/randomkit.c and here : https://github.com/numpy/numpy/blob/master/numpy/random/mtrand/mtrand.pyx#L4669



def plot_sampling(func):
    # I am not sure about testing the distribution..
    print(func)
    list_res = []
    A = range(0, 100)
    for i in range(100000):
        new_val = func(A, 10)
#        print(new_val)
#        print(len(set(new_val)))
        if len(new_val) != len(set(new_val)):
            import IPython
            IPython.embed()

        assert(len(new_val) == len(set(new_val)))
        list_res.extend(new_val)

    pylab.figure()
    pylab.hist(list_res, bins=100, alpha=0.5)


plot_sampling(sample_offline_data_numpy)
plot_sampling(sample_offline_data_rec)
plot_sampling(old_sample_offline_data)
pylab.show()
