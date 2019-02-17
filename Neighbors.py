#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:43:25 2019

@author: felix
"""
from HammingDistance import hamming_distance
from itertools import product


def neighbors(pattern, d):
    neighborhood = set()
    neighborhood.add(pattern)
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    suffix_neighbors = list([''.join(p) for p in product(['A', 'C', 'G', 'T'],
                             repeat=len(pattern))])
    for text in suffix_neighbors:
        if hamming_distance(pattern, text) == d:
            neighborhood.add(text)
    return neighborhood


def Neighbors(Pattern, d, nucleotides={'A', 'C', 'G', 'T'}):
    if d == 0:
        return Pattern
    elif len(Pattern) == 1:
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if hamming_distance(Pattern[1:], Text) < d:
            for x in nucleotides:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return Neighborhood


if __name__ == '__main__':
    with open('test_file.txt', 'w+') as file:
        print(len(list(neighbors('ACGT', 3))))
        print(len(list(Neighbors('ACGT', 3))))
        #for i in list(neighbors('ACGT', 3)):
            #print(i)
            # file.write(i + '\n')
