#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n: int) -> int:
    '''minimum operations on a file'''
    operationsUsedCount = 0
    s = 1
    c = 0

    while s < n:
        if n % s == 0:
            c = s
            s *= 2
            operationsUsedCount += 1
        else:
            s += c

        operationsUsedCount += 1

    return operationsUsedCount
