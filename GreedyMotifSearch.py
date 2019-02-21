#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:16:02 2019

@author: felix
"""
from MotifEnumeration import motif_enumeration
from MotifProfile import find_consensus_motif as fcm
from HammingDistance import hamming_distance as hd
from MotifProfile import profile_laplace as pl
from ProfileMostProblem import profile_most_probable as pmb


def greedy_motif_search(k, t, dna):
    best_motifs = list([dna[i][0: k] for i in range(len(dna))])
    for motif1 in list([dna[0][i: i+k] for i in range(len(dna[0]) - k + 1)]):
        motifs = [motif1, ]
        for i in range(1, t):
            motifs.append(pmb(dna[i], k, pl(motifs)))
        if motif_score(motifs) < motif_score(best_motifs):
            best_motifs = motifs
    return best_motifs


def motif_score(motif_list):
    scores = []
    x = fcm(motif_list)
    for i in motif_list:
        scores.append(hd(x, i))
    return sum(scores)



if __name__ == '__main__':
    k = 3
    t = 5
    dna = [
            'GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC',
            'CACGTCAATCAC', 'CAATAATATTCG'
            ]
#    print(greedy_motif_search(int(k), int(t), dna))
    lines = None
    with open('dataset_160_9.txt', 'r+') as file:
        lines = file.readlines()
    k, t = lines[0].split(' ')
    dna = list([l.strip() for l in lines[1:]])
    for x in greedy_motif_search(int(k), int(t), dna):
        print(x)