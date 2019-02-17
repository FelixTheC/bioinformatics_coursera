#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:10:52 2019

@author: felix
"""


def minimum_skew(genome):
    """
    GC-skew such a useful tool for identifying the location of ori
    """
    val = [0]
    j = 0
    _min = 0
    for i in genome:
        if i == 'C':
            j -= 1
        if i == 'G':
            j += 1
        val.append(j)
    _min = min(val)
    min_pos = list([x for x, i in enumerate(val) if i == _min])
    return min_pos


if __name__ == '__main__':
    with open('vibrio_cholerae.txt', 'r+') as file:
        genome = ''.join(file.readlines())
        print(len(genome))
        #genome='GATACACTTCCCGAGTAGGTACTG'
        print(list([str(i) for i in minimum_skew(genome)]))
