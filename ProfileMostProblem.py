#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:21:30 2019

@author: felix
"""


def profile_most_probable(dna, k, matrix):
    prob_str = {}
    highest = 0
    if isinstance(matrix, dict):
        profile = matrix
    else:
        profile = {'A': matrix[0], 'C': matrix[1], 'G': matrix[2], 'T': matrix[3]}
    for i in range(len(dna) - k + 1):
        text = dna[i: i+k]
        prob = 0
        for index, char in enumerate(text):
            if index == 0:
                prob = profile[char][index]
            else:
                prob *= profile[char][index]
        prob_str[prob] = text
        if prob > highest:
            highest = prob
    return prob_str[highest]


#CCGAG
if __name__ == '__main__':
    lines = []
    dna = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    k = 5
    matrix = [
            [0.2, 0.2, 0.3, 0.2, 0.3],  # A
            [0.4, 0.3, 0.1, 0.5, 0.1],  # C
            [0.3, 0.3, 0.5, 0.2, 0.4],  # G
            [0.1, 0.2, 0.1, 0.1, 0.2],  # T
            ]
#    with open('dataset_159_3.txt', 'r+') as file:
#        lines = file.readlines()
#    
#    dna = lines[0].strip()
#    k = int(lines[1])
#    for i in range(2, 6):
#        matrix.append(list([float(j) for j in lines[i].split('\n')[0].split(' ')]))
    print(profile_most_probable(dna, k, matrix))