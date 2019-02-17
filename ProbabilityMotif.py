#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:38:02 2019

@author: felix
"""
from math import pow
from itertools import combinations
import scipy.misc as sc


def proba_motif(nucleotide_len, len_kmer, nbr_impl):
    ps = list([nucleotide_len - len_kmer + i for i in range(nbr_impl + 1)])
    res = 0
    for p in ps:
        print(p)
        if res == 0:
            res = p
        else:
            res /= p
    _ = pow(res, 10)
    return 1 - _


def proba_motif_2():
    p1 = float ((600 - 15) / (600 - 15 + 1))
    p2 = 1 - p1
    counter = sum(list([1 for seq in combinations(range(10),2)]))
    sc.comb(10, 2, exact=True)
    print(pow(p2,2) * pow(p1,8) * counter)


if __name__ == '__main__':
    print(proba_motif_2())