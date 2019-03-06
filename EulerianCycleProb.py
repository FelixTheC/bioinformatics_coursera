#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:11:35 2019

@author: felix
"""
import copy
import time
from random import choice

def graph(starting, node_edge):
    b = copy.deepcopy(node_edge)
    steps = []
    x = starting
    steps.append(starting)
    while True:
        try:
            if len(b[x]) >= 1:
                x, y = b[x][0], x
                b[y] = list([i for i in b[y] if i != x])
                steps.append(x)
            else:
                x = None
                break
        except KeyError:
            break
    return steps, b

def ordering_edges(edges, node_edge):
    edge = dict()
    for i in edges:
        g, _ = graph(i, node_edge)
        edge[i] = len(g)
    edge = list([i[0] for i in sorted(edge.items(), key=lambda x: x[1], reverse=True)])
    return edge

def eulerian_cycle_prob(node_edges_list):
    node_edge = dict()
    cycles = []
    keys = []
    for index, elem in enumerate(node_edges_list):
        x = elem.replace(' ','').split('->')
        node_edge[x[0]] = list([i.strip() for i in x[1].split(',')])
    for key, val in node_edge.items():
        if len(val) > 1:
            node_edge[key] = ordering_edges(val, node_edge)
    length = sum(list([len(i) for i in node_edge.values()]))
    keys = list([i for i in node_edge.keys()])
    start_edge = 0
    while True:
        tmp = copy.deepcopy(node_edge)
        for x in keys[start_edge:]:
            result, tmp = graph(x, tmp)
            if len(result) == length + 1:
                cycles.append(result)
        if len(cycles) == 0:
            start_edge += 1
        else:
            break
    return cycles


if __name__ == '__main__':
#    edges = [
#            '0 -> 3',
#            '1 -> 0',
#            '2 -> 1, 6',
#            '3 -> 2',
#            '4 -> 2',
#            '5 -> 4',
#            '6 -> 5,8',
#            '7 -> 9',
#            '8 -> 7',
#            '9 -> 6',
#            ]
#    edges = [
#            '0 -> 2',
#             '1 -> 3',
#             '2 -> 1',
#             '3 -> 0,4',
#             '6 -> 3,7',
#             '7 -> 8',
#             '8 -> 9',
#             '9 -> 6',
#            ]
    edges = [
            '1 -> 10',
            '10 -> 2,3,4',
            '2 -> 1',
            '3 -> 10',
            '4 -> 5',
            '5 -> 10',
            ]
#    edges = [
#            '0 -> 1,2,3,4',
#            '1 -> 0,2,3,4',
#            '2 -> 0,1,3,4',
#            '3 -> 0,1,2,4',
#            '4 -> 0,1,2,3',
#            ]
    node_edge = dict()
    for index, elem in enumerate(edges):
        x = elem.replace(' ','').split('->')
        node_edge[x[0]] = list([i.strip() for i in x[1].split(',')])
        
#    print(ordering_edges(['0', '4'], node_edge))
    for i in eulerian_cycle_prob(edges):
        print(i)
