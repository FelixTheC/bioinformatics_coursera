#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:01:07 2019

@author: felix
"""

# fill in your FrequentWords() function here along with any subroutines you need.
def frequent_words(Text, k):
    kmean = {}
    for i in range(0, (len(Text) - k)+1):
        if Text[i:(i+k)] in kmean:
            kmean[Text[i:(i+k)]] += 1
        else:
            kmean[Text[i:(i+k)]] = 0
    most = max(list(kmean.values()))
    return sorted(list([k for k,v in kmean.items() if v == most]))

if __name__ == '__main__':
    print(frequent_words('ATTTGGC', 3))