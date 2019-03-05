#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:35:35 2019

@author: felix
"""
from collections import defaultdict
from collections import OrderedDict


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


def debrujin_graph_problem(dna_list):
    d_suff = defaultdict(str)
    d_pref = defaultdict(list)
    k = len(dna_list[0])
    suffix = list([x[1:] for x in dna_list])
    prefix = list([x[:k-1] for x in dna_list])
    for i, motif in enumerate(suffix):
        d_suff[i] = motif
    for i, motif in enumerate(prefix):
        d_pref[motif].extend([i, ])
    for pkey, pval in d_pref.items():
        d_pref[pkey] = sorted(list([val for key, val in d_suff.items() if key in pval]))
    print(d_suff)
    print(d_pref)
    return OrderedDict(sorted(d_pref.items()))


if __name__ == '__main__':
    motif_matrix = ['GCGA',
                    'CAAG',
                    'AAGA',
                    ]
    print(debrujin_string_problem(4, '0101010100'))
#    lines = []
#    with open('dataset_200_8.txt', 'r+') as file:
#        lines = file.readlines()
#    text = list([l.strip() for l in lines])
#    with open('tmp.txt', 'w+') as file:
#        for key, val in debrujin_graph_problem(lines).items():
#            _ = ','.join(val)
#            file.write(f'{key}->{_}\n')
#    lines = []
#    with open('dataset_199_6.txt', 'r+') as file:
#        lines = file.readlines()
#    k = int(lines[0].strip())
#    dna = lines[1].strip()
#    with open('tmp.txt', 'w+') as file:
#        for key, val in debrujin_string_problem(k, dna).items():
#            _ = ','.join(val)
#            file.write(f'{key}->{_}\n')
#    lines = []
#    with open('dataset_198_10.txt', 'r+') as file:
#        lines = file.readlines()
#    text = list([l.strip() for l in lines])
#    print(reconstruction_problem(text))
#    with open('tmp.txt', 'w+') as file:
#        for key, val in reconstruction_walk_problem(text).items():
#            _ = ','.join(val)
#            file.write(f'{key}->{_}\n')
