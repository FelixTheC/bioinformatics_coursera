#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:51:12 2019

@author: felix
"""


def generate_composition(kmer, string):
    compositions = []
    for i in range(len(string) - kmer[0] - kmer[1] - 2):
        a = string[i: i + kmer[0]]
        b = string[i + kmer[0] + kmer[1]: i + kmer[1] + kmer[0] + kmer[0]]
        print(a, b)
        compositions.append((a, b))
    return list(sorted(compositions))


if __name__ == '__main__':
    with open('composition.txt', 'w+') as file:
        for x in generate_composition((3, 1), 'TAATGCCATGGGATGTT'):
            file.write(f'({x[0]}|{x[1]}) ')
