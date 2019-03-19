#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: felix
"""
from collections import Counter

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


def theoretical_spectrum(peptide):
    cyclospectrum = [0, ]
    x = list(peptide)
    for j in range(1, len(peptide)):
        for i in range(0, len(peptide)):
            y = x[i: i + j]
            if len(y) < j:
                y.extend(x[0: j - len(y)])
            cyclospectrum.append(sum([INTEGERMASS[acid] for acid in y]))
        cyclospectrum.append(sum(INTEGERMASS[acid] for acid in x))
    return cyclospectrum


def cyclopeptide_scoring(peptide, spectrum):
    score = 0
    peptide_dict = Counter(theoretical_spectrum(peptide))
    scoring_dict = Counter(spectrum)
    for pep_key, pep_val in peptide_dict.items():
        try:
            x = scoring_dict[pep_key]
            if x > pep_val:
                score += pep_val
            else:
                score += x
        except KeyError:
            print(f'{pep_key} not in scoring')
    return score


if __name__ == '__main__':
    test_peptide = 'VYYEVDWTMGRQIDPDEYPIAQCTRHRATILTLPDWQM'
    test_result = 521
    test_spectrum = list([int(i) for i in open('files/test_cyclopeptide_scoring.txt', 'r+').readline().split(' ')])
    #print(cyclopeptide_scoring('NQEL', [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]))
    result = cyclopeptide_scoring(test_peptide, test_spectrum)
    if result == test_result:
        print('Test passed')
    else:
        print('Test NOT passed')
