#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:06:49 2019

@author: felix
"""
import pickle


class GeneticCode(object):
    filename = 'genetic_code'
    x = {}
    
    def __init__(self, *args, **kwargs):
        self._input_(*args)
        
    def __getitem__(self, y):
        try:
            return self.x[y]
        except KeyError:
            raise KeyError
        
    def get(self, k, d=None):
        try:
            return x[k]
        except KeyError:
            if d is None:
                raise KeyError(f'{k} not in dict')
            else:
                return d
    
    def _input_(self, *args):
        for elem in args:
            y = dict(elem)
            for key, val in y.items():
                self.x[key] = val

    def save_dict(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.x, file, pickle.HIGHEST_PROTOCOL)

    def load_dict(self):
        with open(self.filename, 'rb') as file:
            self.x = pickle.load(file)


if __name__ == '__main__':
    genetic_code = GeneticCode(
            {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 
             'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
             'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
             'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
             'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
             'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
             'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
             'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
             'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
             'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '*', 'UAC': 'Y',
             'UAG': '*', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S',
             'UCU': 'S', 'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C',
             'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F',
             }
            )
    genetic_code.filename = 'genetic_code'
    genetic_code.save_dict()
