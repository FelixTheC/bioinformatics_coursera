#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:40:47 2019

@author: felix
"""
import time

def checktime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = (time.time() - start) / 60
        print(f'{func.__name__}\t{end}')
        return f
    return wrapper


def get_subtraction(Genome, L):
    liste = [(0, L)]
    rest = len(Genome)
    while rest > L:
        rest = abs(rest - L)
        if abs(len(Genome) - rest) > abs(len(Genome) - L):
            liste.append(( len(Genome) - rest, len(Genome) ))
        else:
            liste.append(( len(Genome) - rest, len(Genome) - rest + L ))
    return liste


def ClumpFinding(Genome, k, L, t):
    final_array = []
    for h in get_subtraction(Genome, L):
        end = h[1] if h[1] < len(Genome) else h[1]
        for i in range(h[0], end):
            init_dict = {}
            kmer = Genome[i: i+L]
            for x in range(len(kmer)):
                if kmer[x: x+k] in init_dict:
                    init_dict[kmer[x: x+k]] += 1
                else:
                    init_dict[kmer[x: x+k]] = 1
            final_array.extend(list([key for key, val in init_dict.items() if val == t]))
    return list(set(final_array))

if __name__ == '__main__':
    #genome = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
    counter = 0
    with open('ecoli.txt', 'r+') as file:
        genome = file.readlines()
        for i in genome:
            print(i)
            i = i.replace('\n', '')
            counter += len(ClumpFinding(i, 9, 500, 3))
    print(counter)















    