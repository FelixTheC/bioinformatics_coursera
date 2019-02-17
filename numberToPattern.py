#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:08:12 2019

@author: felix
"""

def number_to_pattern(num, k):
    pat_num_dic = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    pattern = []
    while k > 0:
        pattern.append(pat_num_dic[num%4])
        num = num // 4
        k -= 1
    return ''.join(pattern[::-1]) 

if __name__ == '__main__':
    print(number_to_pattern(25, 3))