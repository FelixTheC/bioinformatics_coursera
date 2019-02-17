#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:15:15 2019

@author: felix
"""

def pattern_matching(pattern, genome):
    start_pos = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i: i + len(pattern)] == pattern:
            start_pos.append(str(i))
    if len(start_pos) == 1:
        return start_pos[0]
    else:
        return ' '.join(start_pos)


if __name__ == '__main__':
#    with open('Vibrio_cholerae.txt', 'r+') as file:
#        text = file.readline()
#        print(text)
    print(pattern_matching('ATA', 'GACGATATACGACGATA'))