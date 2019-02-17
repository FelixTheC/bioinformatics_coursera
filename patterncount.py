#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:00:25 2019

@author: felix
"""

def find_most_outcome(text, pattern):
    most = {}
    for i in range(0, len(text), pattern):
        if text[i:(i+pattern)] in most:
            most[text[i:(i+pattern)]] += 1
        else:
            most[text[i:(i+pattern)]] = 0
    return most

def pattern_count(Text, Pattern):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Text[i: (i + len(Pattern))] == Pattern:
            count += 1
    return count


if __name__ == '__main__':
    print(pattern_count('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC', 'CGCG'))