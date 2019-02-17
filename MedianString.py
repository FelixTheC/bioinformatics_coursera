#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 08:57:20 2019

@author: felix
"""
from itertools import product
from DistanceBetweenPatternStrings import distance_between_pattern_and_strings as d


def median_string(dna, k):
    median = ''
    distance = 100
    for i in list([''.join(p) for p in product(['A', 'C', 'G', 'T'], repeat=k)]):
        if median == '':
            median = i
        result = d(i, dna)
        if i in ['AACGCTG', 'GAACCAC', 'CGTGTAA', 'ATAACGG', 'AATCCTA', 'GGTTACT']:
            print(f'{i}: {result}')
        if result < distance:
            distance = result
            median = i
    return median


if __name__ == '__main__':
    lines = []
    k = 7
    dna = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
           'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
           'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG',
           ]
#    with open('dataset_158_9.txt', 'r+') as file:
#        lines = file.readlines()
#    pattern = lines[0].strip()
#    dna = np.concatenate([l.split(' ') for l in lines[1:]])
    print(median_string(dna, k))
