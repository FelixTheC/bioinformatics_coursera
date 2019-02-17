#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:53:20 2019

@author: felix
"""
from random import choice
from MotifProfile import profile_laplace as pl
from MotifProfile import find_consensus_motif as fcm
from ProfileMostProblem import profile_most_probable as pmb
from HammingDistance import hamming_distance as hd


def randomized_motif_single_search(dna, k, t):
    rnd_motifs = list([select_random_motif(j, k) for j in dna])
    best_motifs = rnd_motifs
    while True:
        profile = pl(best_motifs)
        motifs = list([pmb(j, k, profile) for j in dna])
        if motif_score(motifs) < motif_score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


def gibbs_sampler_one(dna, k, t, n):
    rnd_motifs = list([select_random_motif(j, k) for j in dna])
    best_motifs = rnd_motifs
    for i in range(n):
        i = choice(list(x for x in range(0, t)))
        motifs_no_i = best_motifs.copy()
        del motifs_no_i[i]
        profile = pl(motifs_no_i)
        motifi = list([pmb(j, k, profile) for j in dna])
        motifi[i] = select_random_motif(dna[i], k)
        motifs = motifi
        if motif_score(motifs) < motif_score(best_motifs):
            best_motifs = motifs
    return best_motifs


def select_random_motif(text, k):
    t = list([i for i in range(len(text) - k + 1)])
    x = choice(t)
    return text[x:x+k]
    

def motif_score(motif_list):
    scores = []
    x = fcm(motif_list)
    for i in motif_list:
        scores.append(hd(x, i))
    return sum(scores)


def randomly_gernated_kmer(motif, k):
    _ = ''.join(motif)
    rnd_motif = ''
    for i in range(k):
        rnd_motif += choice(_)
    return rnd_motif


def randomized_motif_search(dna, k, t):
    best = []
    for i in range(1000):
        resp = randomized_motif_single_search(dna, k, t)
        if len(best) == 0:
            best = resp
        else:
            if motif_score(best) > motif_score(resp):
                best = resp
    return best


def gibbs_sampler(dna, k, t, n):
    best = []
    for i in range(19):
        resp = gibbs_sampler_one(dna, k, t, n)
        if len(best) == 0:
            best = resp
        else:
            if motif_score(best) > motif_score(resp):
                best = resp
    return best


if __name__ == '__main__':
    lines = []
    dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
           'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
           'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
           'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
           'AATCCACCAGCTCCACGTGCAATGTTGGCCTA',
           ]
    k = 8
    t = 5
    n = 100
#    with open('dataset_163_4.txt', 'r+') as file:
#        lines = file.readlines()
#    
#    k, t, n = lines[0].split(' ')
#    dna = list([l.strip() for l in lines[1:]])
    res = gibbs_sampler(dna, int(k), int(t), int(n))
    for i in res: 
        print(i)
    
#    test = ['AAGCCAAA', 'AATCCTGG', 'GCTACTTG', 'ATGTTTTG']
#    print(randomized_motif_search(test, 3, 4))
