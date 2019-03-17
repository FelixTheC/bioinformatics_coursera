#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:50:59 2019

@author: felix
"""

from reverse_complement import reverse_complement

GENETICCODE = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 
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


def peptide_encoding(dna, genetic_code):
    rna = dna.replace('T', 'U')
    rrna = reverse_complement(dna).replace('T', 'U')
    length = 3 * len(genetic_code)
    peptides = []
    for i in range(0, len(rna) - length):
        gen_code = ''
        rgen_code = ''
        peptide = rna[i: i + length]
        rpeptide = rrna[i: i + length]
        for j in range(0, len(peptide), 3):
            rgen_code += GENETICCODE[rpeptide[j: j + 3]]
            gen_code += GENETICCODE[peptide[j: j + 3]]
        if gen_code == genetic_code:
            peptides.append(peptide.replace('U', 'T'))
        elif rgen_code == genetic_code:
            peptides.append(peptide.replace('U', 'T'))
    return peptides


def aminoacid_DNA_codons(): 
    aminoacidToDNACodons = {}
    for k,v in GENETICCODE.items():
        aminoacidToDNACodons.setdefault(v, []).append(k)
    return aminoacidToDNACodons


def times_dna(peptide='LWK'):
    n = 1
    codons = aminoacid_DNA_codons()
    for i in range(len(peptide)):
        n*=len(codons[peptide[i]])
    return n


def number_subpeptides(n):
    return  n*(n-1)


def number_linear_subpeptides(n):
    return int(n*(n + 1)/2 + 1)


if __name__ == '__main__':
    print(times_dna('CYCLIC'))
    print(number_subpeptides(1024))
#    dna = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
#    lines = []
#    genetic_code = 'VKLFPWFNQY'
#    with open('files/Bacillus_brevis.txt', 'r+') as file:
#        lines = file.readlines()
#        lines = list([i.strip() for i in lines])
#    dna = ''.join(lines)
#    print(len(peptide_encoding(dna, genetic_code)))
