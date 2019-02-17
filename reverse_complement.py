#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 06:29:23 2019

@author: felix
"""

def reverse_complement(dna):
    comlement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    dna = dna.replace('\n', '')
    return ''.join(list([comlement[i] for i in dna[::-1]]))


if __name__ == '__main__':
    print(reverse_complement('GCTAGCT'))