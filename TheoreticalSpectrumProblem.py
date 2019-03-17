#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:00:53 2019

@author: felix
"""
from itertools import combinations

INTEGERMASS = {
                'G': 57,
                'A': 71,
                'S': 87,
                'P': 97,
                'V': 99,
                'T': 101,
                'C': 103,
                'I': 113,
                'L': 113,
                'N': 114,
                'D': 115,
                'K': 128,
                'Q': 128,
                'E': 129,
                'M': 131,
                'H': 137,
                'F': 147,
                'R': 156,
                'Y': 163,
                'W': 186,
                }


def theoretical_spectrum_problem(peptide):
    cyclospectrum = [0, ]
    x = list(peptide)
    for j in range(1, len(peptide)):
        for i in range(0, len(peptide)):
            y = x[i: i + j]
            if len(y) < j:
                y.extend(x[0: j - len(y)])
            cyclospectrum.append(sum([INTEGERMASS[acid] for acid in y]))
    cyclospectrum.append(sum([INTEGERMASS[acid] for acid in x]))
    return list(sorted(cyclospectrum))


def theoretical_linear_spectrum_problem(peptide):
    cyclospectrum = [0, ]
    x = list(peptide)
    for j in range(1, len(peptide)):
        for i in range(0, len(peptide)):
            y = x[i: i + j]
            if len(y) == j:    
                cyclospectrum.append(sum([INTEGERMASS[acid] for acid in y]))
    cyclospectrum.append(sum([INTEGERMASS[acid] for acid in x]))
    return list(sorted(cyclospectrum))
            


if __name__ == '__main__':
    print(theoretical_spectrum_problem('CTV'))
#    with open('cyclospectrum2.txt', 'w+') as file:
#        for i in theoretical_linear_spectrum_problem('GCMQSPKKAHDMPEQFMRRICQYCQYWVRCNTPIIYPRYEDNLDQMTH'):
#            file.write(f'{i} ')