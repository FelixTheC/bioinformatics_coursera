#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:35:35 2019

@author: felix
"""
from collections import defaultdict


def reconstruction_problem(motif_matrix):
    dna = motif_matrix[0]
    for motif in motif_matrix[1:]:
        dna += motif[-1]
    return dna


def reconstruction_walk_problem(motif_matrix):
    findings = dict()
    if len(motif_matrix) == 1:
        return {motif_matrix[0]: motif_matrix[0]}
    for motif in motif_matrix:
        res = list(set([i for i in motif_matrix if motif[1:] in i and motif != i]))
        if len(res) > 0: 
            findings[motif] = res
    return findings


def debrujin_string_problem(k, dna):
    n = k - 1
    m = k - 2
    d = defaultdict(list)
    d2 = defaultdict(list)
    matrix = list([dna[i: i+n] for i in range(len(dna) - n + 1)])
    for i, motif in enumerate(matrix[1:]):
        d2[motif].extend([i, ])
    for i, motif in enumerate(matrix):
        tmp = list([x for x,v in d2.items() if i in v])
        if len(tmp) > 0:
            res = list([x for x in tmp if motif[1:] == x[:m]])
            d[motif].extend(res)
    return d


if __name__ == '__main__':
    motif_matrix = ['CT', 'TG',
                    'TG', 'TC',
                    'TT', 'TC',
                    ]
    lines = []
    with open('dataset_199_6.txt', 'r+') as file:
        lines = file.readlines()
    k = 4 #  int(lines[0].strip())
    dna = 'AGCCT' #  lines[1].strip()
    with open('tmp.txt', 'w+') as file:
        for key, val in debrujin_string_problem(k, dna).items():
            _ = ','.join(val)
            print(f'{key}->{_}')
            #file.write(f'{key}->{_}\n')
#    lines = []
#    with open('dataset_198_10.txt', 'r+') as file:
#        lines = file.readlines()
#    text = list([l.strip() for l in lines])
#    print(reconstruction_problem(text))
#    with open('tmp.txt', 'w+') as file:
#        for key, val in reconstruction_walk_problem(text).items():
#            _ = ','.join(val)
#            file.write(f'{key}->{_}\n')
