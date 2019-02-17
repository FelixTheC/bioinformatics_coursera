#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:23:14 2019

@author: felix
"""
from Neighbors import Neighbors
from HammingDistance import hamming_distance
import numpy as np


def motif_enumeration(dna, k, d):
    _ = dict()
    for j in dna:
        if d != 0: 
            patterns = np.concatenate([Neighbors(j[i: i+k], d) for i in range(len(j) - k + 1)])
        else:
            patterns = list([Neighbors(j[i: i+k], d) for i in range(len(j) - k + 1)])
        for i in list(set(patterns)):
            if i in _:
                _[i] += 1
            else:
                _[i] = 1
    dmax = max(list([i for i in _.values()]))
    if dmax >= len(dna):
        return list([key for key, val in _.items() if val == dmax])
    else:
        return []

            

if __name__ == '__main__':
    dna = ['CGCTGTATTTGGCGACCACCGCCGA', 'GATTCTAGACGTCAGCGCGGAAGTA',
           'CGCAGGAGGCGTACCGCCCCTGCTG', 'ATTAACATGAATTGCCGCTGAACTT',
           'ACAAAGGGGGATATCCGCTGTAACC', 'TCGATTGCAGTAACGGTTGTCGCCG']
    k = 5
    d = 1
    print(' '.join(list(sorted(motif_enumeration(dna, k, d)))))
        