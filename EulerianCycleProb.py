#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:11:35 2019

@author: felix
"""
import copy
import time
from random import choice

def eulerian_cycle_prob(node_edges_list):
    node_edge = dict()
    cycles = []
    keys = []
    stop= '0'
    for index, elem in enumerate(node_edges_list):
        x = elem.replace(' ','').split('->')
        node_edge[x[0]] = list([i.strip() for i in x[1].split(',')])
    length = sum(list([len(i) for i in node_edge.values()]))
    keys = list([i for i in node_edge.keys()])
    stop = '0' #node_edge[keys[0][0]][0]
    for i in range(length):
        for x in keys:
            cycle = []
            tmp = copy.deepcopy(node_edge)
            while True:
                cycle.append(x)
                try:
                    x, y = choice(tmp[x]), x
                except (IndexError, TypeError):
                    break
                tmp[y] = list([i for i in tmp[y] if i != x])
            if cycle[0] == cycle[-1] and len(cycle) == length + 1 and cycle[0] == stop:
                cycles.append(cycle)
                break
    return cycles
                
    
    
    
if __name__ == '__main__':
    edges = [
            '0 -> 3, 1',
            '1 -> 2',
            '2 -> 0',
            '3 -> 0',
            ]
    for i in eulerian_cycle_prob(edges):
        print(i)
