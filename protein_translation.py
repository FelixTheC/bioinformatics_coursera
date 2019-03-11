#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:05:24 2019

@author: felix
"""
from genetic_code import GeneticCode

def protein_translation_problem(rna):
    amino_acid_str = ''
    gen_code = GeneticCode()
    gen_code.filename = 'genetic_code'
    gen_code.load_dict()
    
    for i in range(0, len(rna) - 3, 3):
        amino_acid_str += gen_code[rna[i: i + 3]]
    return amino_acid_str


if __name__ == '__main__':
    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    print(protein_translation_problem(rna))