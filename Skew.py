#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 20:59:26 2019

@author: felix
"""

'   C  A  T G G G C A T C G G C C A T A  C G  C  C'
'0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'


def get_skew(genome):
    val = [0]
    j = 0
    for i in genome:
        if i == 'C':
            j -= 1
        if i == 'G':
            j += 1
        val.append(j)
    return val


if __name__ == '__main__':
    genome = 'CCGGCCGG'
    print(' '.join(list([str(i) for i in get_skew(genome)])))
