#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: felix
"""
from CyclopeptideScoringProblem import cyclopeptide_linear_scoring


def trim(leaderboard, spectrum, n):
    n = int(n)
    linear_scores = dict()
    linear_scores_keys = []
    for j in leaderboard:
        linear_scores[j] = cyclopeptide_linear_scoring(j, spectrum)
    linear_scores = dict(sorted(linear_scores.items(), key=lambda x: x[1], reverse=False))
    limit_score = list(linear_scores.values())[n * -1]
    for key, val in linear_scores.items():
        if val >= limit_score:
            linear_scores_keys.append(key)
    return linear_scores_keys


if __name__ == '__main__':
    leaderboard = ['LAST', 'ALST', 'TLLT', 'TQAS']
    spectrum = [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372]
    n = 2
    lines = []
    print(trim(leaderboard, spectrum, n))
    with open('trim_test.txt', 'r+') as file:
        lines = file.readlines()
    leaderboard = lines[1].replace('\n', '').split(' ')
    spectrum = list([int(i) for i in lines[2].replace('\n', '').split(' ')])
    n = lines[3].strip()
    result = trim(leaderboard, spectrum, n)
    expected_result = lines[-1].replace('\n', '').split(' ')
    if sorted(result) == sorted(expected_result):
        print('test passed')
