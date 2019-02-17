#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:24:12 2019

@author: felix
"""

def pattern_to_number(pattern):
    pat_num_dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num = 0
    for i, pat in enumerate(reversed(pattern)):
        num += pat_num_dic[pat] * (4**i)
    return num

def computing_frequencies(Text, k):
    frequency_array = list([0 for i in range(4**k)])
    for i in range(0, len(Text) - (k-1)):
        pattern = Text[i: i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array


if __name__ == '__main__':
    with open('dataset_2994_5.txt', 'r+') as file:
        text = file.readline().replace('\n', '')
        #text = 'AAAAC'
        print(' '.join(list([ str(i) for i in computing_frequencies(text, 7)])))