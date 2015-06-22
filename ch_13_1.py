# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Laurent George.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""

# chapter 13 hassing table
# exercise 1
# debut : 16h57 21 juin
# fin : 17h22 21 juin, duration = 25 min

from collections import OrderedDict

def anagrams(word_set):
    """
    return groups of anagrams for words in `word_set`

    Complexity is :

    O(klogk) * n + n*O(1) for insertion in dict + O(n) (for the return loop where we count number of word)
    ~= O(n*klog(k)) with n number of word and k the maximum number of character per string

    sort complexity is O(klogk) for a word of k letters

    we use OrderedDict which allow easy comparison for doctest.. but it's not
    mandatory at all
    >>> anagrams(["debitcard", "elvis", "silent", "badcredit", "lives",\
    "freedom", "listen", "levis"])
    [set(['debitcard', 'badcredit']), set(['levis', 'elvis', 'lives']), set(['silent', 'listen'])]
    >>> anagrams([])
    []
    """
    words_grouped_by_sorted_words = OrderedDict()
    for word in word_set:
        sorted_word = ''.join(sorted(word))
        if not(sorted_word in words_grouped_by_sorted_words):
            words_grouped_by_sorted_words[sorted_word] = set([])
        words_grouped_by_sorted_words[sorted_word].add(word)

    return [x for x in words_grouped_by_sorted_words.values() if len(x)>1]
