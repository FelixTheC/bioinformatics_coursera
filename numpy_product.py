#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:34:57 2019

@author: felix
"""
import numpy as np


def create_products(list_obj, times):
    if isinstance(list_obj, list):
        t = list([list_obj for _ in range(times)])
        return np.array(np.meshgrid(*t)).T.reshape(-1, times)
    else:
        raise TypeError(f'{list_obj} must be list instance')


if __name__ == '__main__':
    INTEGERMASS = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        #'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        #'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186,
    }
    INTEGERMASS_2 = {
        57: 'G',
        71: 'A',
        87: 'S',
        97: 'P',
        99: 'V',
        101: 'T',
        103: 'C',
        113: 'I',
        114: 'N',
        115: 'D',
        128: 'K',
        129: 'E',
        131: 'M',
        137: 'H',
        147: 'F',
        156: 'R',
        163: 'Y',
        186: 'W',
    }
    spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
    total = 4 * len(set(spectrum))
    possible_results = list(list() for i in range(total))
    result = []
    x = list(INTEGERMASS.keys())
    for spec in spectrum[1:]:
        y = create_products(x, int(round(spec/100)))
        get_val = lambda v: INTEGERMASS[v]
        for val in y:
            try:
                if sum(set([INTEGERMASS[x] for x in val])) == spec:
                    print(val, sum(set([INTEGERMASS[x] for x in val])))
            except TypeError:
                print(val)

    print(result)
    print(list(set(''.join(result))))
