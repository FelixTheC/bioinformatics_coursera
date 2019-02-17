#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:16:02 2019

@author: felix
"""
from MotifEnumeration import motif_enumeration


def greedy_motif_search(k, t, dna):
    best_motifs = []
    for j in dna:
        texte = []
        for i in range(len(j) - k + 1):
            texte.append(j[i: i + k])
        print(texte)
        motifs = motif_enumeration(texte, k, t)
        print(motifs)
    return best_motifs


if __name__ == '__main__':
    k = 3
    t = 5
    dna = [
            'GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC',
            'CACGTCAATCAC', 'CAATAATATTCG'
            ]
    print(greedy_motif_search(k, t, dna))