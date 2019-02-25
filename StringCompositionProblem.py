#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:18:14 2019

@author: felix
"""

def composition_problem(text, k):
    return list([text[i: i+k] for i in range(len(text) - k + 1)])


if __name__ == '__main__':
    text = 'GGGGGGTGGG'
    k = 3
    lines = []
    with open('dataset_197_3.txt', 'r+') as file:
        lines = file.readlines()
    k = int(lines[0].strip())
    text = lines[1].strip()
    with open('tmp_sorted.txt', 'w+') as file:
        _ = '\n'.join(composition_problem(text, k))
        file.write(_)
