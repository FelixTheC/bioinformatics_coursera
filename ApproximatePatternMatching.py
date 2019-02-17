#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:40:44 2019

@author: felix
"""
from HammingDistance import hamming_distance


def approx_pattern_matching(pattern, text, d):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        if len(text[i: i + len(pattern)]) == len(pattern):
            val1 = pattern
            val2 = text[i: i + len(pattern)]
        else:
            val2 = text[i: i + len(pattern)]
            val1 = pattern[:len(val2)]

        if hamming_distance(val1, val2) <= d:
            matches.append(i)
    return matches


def approx_pattern_count(pattern, text, d):
    return len(approx_pattern_matching(pattern, text, d))


if __name__ == '__main__':
    with open('dataset_9_6.txt', 'r+') as file:
#        pattern = file.readline().replace('\n', '')
#        text = file.readline().replace('\n', '')
#        d = int(file.readline())
        pattern = 'TGT'
        text = 'CGTGACAGTGTATGGGCATCTTT'
        d = 1
        res = approx_pattern_count(pattern, text, d)
        print(res)
        # print(' '.join(list([str(i) for i in res])))
