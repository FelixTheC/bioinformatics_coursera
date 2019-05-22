from cpython cimport array
import array

def pattern_to_number(char[] pattern):
    # {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    cdef int num=0, i=0
    cdef char pat
    for i, pat in enumerate(reversed(pattern)):
        if pat == 'A':
            num += 0 * (4**i)
        if pat == 'C':
            num += 1 * (4**i)
        if pat == 'G':
            num += 2 * (4**i)
        if pat == 'T':
            num += 3 * (4**i)
    return num

def computing_frequencies(char[] Text, int k):
    cdef int i=0, j=0, end=0, x=0
    cdef array_size = 4**k
    cdef array.array ca = array.array('i', list([0 for i in range((4**k) + 1)]))
    cdef int[:] frequency_array = ca
    cdef char[7] patterns
    for i in range(0, len(Text) - (k-1)):
        end = i + k
        pattern = Text[i:end]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    return frequency_array