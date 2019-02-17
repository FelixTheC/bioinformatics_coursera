#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:57:22 2019

@author: felix
"""

from Neighbors import neighbors
from reverse_complement import reverse_complement


def frequent_words_missmatch(text, k, d):
    kmean = {}
    for i in range(len(text) - k + 1):
        res = list(neighbors(text[i: i+k], d))
        if d == 0:
            res = [''.join(res), ]
        for j, h in res:
            if j in kmean:
                kmean[j] += 1
            else:
                kmean[j] = 1
    maximum = max(list([val for key, val in kmean.items() if len(key) == k]))
    return list([key for key, val in kmean.items() if val == maximum])


def frequent_words_missmatch_with_reversed(text, k, d):
    kmean = {}
    for i in range(len(text) - k + 1):
        res = list(neighbors(text[i: i+k], d))
        repattern = reverse_complement(text[i: i+k])
        res_reversed = list(neighbors(repattern, d))
        if d == 0:
            res = [''.join(res), ]
            res_reversed = [''.join(res_reversed), ]
        for j, h in zip(res, res_reversed):
            if j in kmean:
                kmean[j] += 1
            else:
                kmean[j] = 1
            if h in kmean:
                kmean[h] += 1
            else:
                kmean[h] = 1
    maximum = max(list([val for key, val in kmean.items() if len(key) == k]))
    return list([key for key, val in kmean.items() if val == maximum])  


if __name__ == '__main__':
    with open('dataset_9_8.txt', 'r+') as file:
        text = file.readline()
        k, d = 5, 3
        print(' '.join(list(frequent_words_missmatch(text, k, d))))