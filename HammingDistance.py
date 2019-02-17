#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:24:29 2019

@author: felix
"""


def hamming_distance(val1, val2):
    if len(val1) == len(val2):
        return sum(list([1 for x, y in zip(val1, val2) if x != y]))
    else:
        raise ValueError('val1 and val2 must have equal lenght')


if __name__ == '__main__':
    with open('dataset_9_3.txt', 'r+') as file:
#        val1 = file.readline()
#        val2 = file.readline()
        val1 = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
        val2 = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
        print(hamming_distance(val1, val2))
