""" A one-line description.

A longer description that spans multiple lines.  Explain the purpose of the
file and provide a short list of the key classes/functions it contains.  This
is the docstring shown when some does 'import foo;foo?' in IPython, so it
should be reasonably useful and informative.
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


def parity_of(x):
    """
    complexity : O(n) with n the number of bits in word x
    >>> parity_of(0b1010)
    0
    >>> parity_of(0b1110)
    1
    """
    result = 0
    while (x  != 0):
        result ^= x & 1
        x >>= 1
    return result

def parityOf(x):
    """
    complexity : O(k) with k number of bits set to 1 in word x
    >>> parityOf(0b1010)
    0
    >>> parityOf(0b1110)
    1
    """
    parity = 0
    while (x!=0):
        #parity = ~parity  <-- on aura -1
        parity ^= 1
        x = x & (x - 1)
    return parity


def parity_of_very_long(x, word_size=8):
    """
    parity of a big word is the xor of the parity of words that compose this big word
    :param x:
    :return:
    """
    res = 0
    hash_map = {}
    while x!=0:
        word = x & ( (1<<word_size)-1)
        if not(word in hash_map):
            hash_map[word] = parityOf(word)
        res ^= hash_map[word]
        x >>= word_size
    print(hash_map)
    return res


