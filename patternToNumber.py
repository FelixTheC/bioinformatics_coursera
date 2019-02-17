#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:09:14 2019

@author: felix
"""

#if A = 0, C = 1, G = 2, T = 3, 
#
#AT is 03 (base 4) = (0 * 4^0) + (3 * 4^1) = 3 (base 10)
#
#TA is 30 (base 4) = (3 * 4^0) + (0 * 4^1) = 12 (base 10)
#
#TT is (3 * 4^1) + (3 * 4^0) = 15. 
#
#ATGCCA = (0 * 4^0) + (1 * 4^1) + (1 * 4^2) + (2 * 4^3) + (3 * 4^4) + (0 * 4^5) (reverse order because it's easier to go up with the powers of 4)

def pattern_to_number(pattern):
    pat_num_dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num = 0
    for i, pat in enumerate(reversed(pattern)):
        num += pat_num_dic[pat] * (4**i)
    return num
        

if __name__ == '__main__':
    print(pattern_to_number('TGCA'))