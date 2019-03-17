#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:09:33 2019

@author: felix
"""

def paired_composition_craph(kmers, node_edges):
    start = ''
    nodes = list([x[0] for x in [i.replace('(', '').replace(')', '').split('|') for i in node_edges]])
    edges = list([x[1] for x in [i.replace('(', '').replace(')', '').split('|') for i in node_edges]])
    
    prefix = paired_composition_craph(nodes, (kmers[1], 1))
    suffix = paired_composition_craph(edges, (kmers[1], 1))
    
    for i in range(kmers[0] + kmers[1] + 1, len(prefix)):
        if prefix[i] != suffix[i]:
             pass
        else:
            start = i
    return prefix + suffix[(kmers[0] + kmers[1]) * -1:]

node_edges = ['(AAT|CCA)', '(ATG|CAT)', '(ATG|GAT)', '(CAT|GGA)',
              '(CCA|GGG)', '(GCC|TGG)', '(GGA|GTT)', '(GGG|TGT)',
              '(TAA|GCC)', '(TGC|ATG)', '(TGG|ATG)']
kmers = (3, 1)


if __name__ == '__main__':
    print(paired_composition_craph(kmers, node_edges))
