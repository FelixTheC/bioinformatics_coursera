#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:12:11 2019

@author: felix
"""
import numpy as np
from HammingDistance import hamming_distance


def distance_between_pattern_and_strings(pattern, dna):
    k = len(pattern)
    distance = 0
    tmp = []
    for text in dna:
        text = text.strip()
        result = list([hamming_distance(text[i: i+k], pattern) for i in range(len(text) - k + 1)])
        try:
            distance += min(result)
        except ValueError:
            pass
    return distance


if __name__ == '__main__':
    dna = []
    lines = None
    with open('dataset_5164_1.txt', 'r+') as file:
        lines = file.readlines()
    pattern = lines[0].strip()
    dna = np.concatenate([l.split(' ') for l in lines[1:]])
#    dna = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG',
#           'GCTGAGCACCGG', 'AGTTCGGGACAG']
#    pattern = 'GAC'
    print('result: ', distance_between_pattern_and_strings(pattern, dna))
