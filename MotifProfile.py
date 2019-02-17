#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:44:47 2019

@author: felix
"""
import numpy as np
from collections import Counter


def profile(dna):
    profile_dic = {'A': [], 'C': [], 'G': [], 'T': []}
    splitter = lambda x: list([i for i in x])
    tmp = np.array(list(map(splitter, dna)))
    for i in range(len(dna[0])):
        _ = Counter(tmp[:, i])
        for x in ['A', 'C', 'G', 'T']:
            profile_dic[x].append(_[x] / 5)
    return profile_dic


def profile_laplace(dna):
    profile_dic = {'A': [], 'C': [], 'G': [], 'T': []}
    splitter = lambda x: list([i for i in x])
    tmp = np.array(list(map(splitter, dna)))
    for i in range(len(dna[0])):
        _ = Counter(tmp[:, i])
        for x in ['A', 'C', 'G', 'T']:
            profile_dic[x].append((_[x] + 1) / 8)
    return profile_dic



def find_consensus_motif(dna):
    consensus_string = ''
    splitter = lambda x: list([i for i in x])
    tmp = np.array(list(map(splitter, dna)))
    for i in range(len(dna[0])):
        _ = Counter(tmp[:, i])
        _max = max(list([i for i in _.values()]))
        consensus_string += list([k for k,v in _.items() if v == _max])[0]
    return consensus_string


if __name__ == '__main__':
    dna = ['TCGGGGGTTTTT', 'CCGGTGGACTAC', 'ACGGGGGATTTC',
           'TTGGGGACTTTT', 'AAGGGGACTTCC', 'TTGGGGACTTCC',
           'TCGGGGATTCAT', 'TCGGGGATTCCT', 'TAGGGGAACTAC',
           'TCGGGTATAACC',
           ]
    print(find_consensus_motif(dna))