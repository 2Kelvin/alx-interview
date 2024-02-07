#!/usr/bin/python3
'''N Queens'''
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

if not sys.argv[1].isdigit():
    print('N must be a number')
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print('N must be atleast 4')
    sys.exit(1)

argN = int(sys.argv[1])


def findQueens(x, i=0, e=[], f=[], g=[]):
    '''find the queens'''
    if i < x:
        for j in range(x):
            if j not in e and i + j not in f and i - j not in g:
                yield from findQueens(
                    x, i + 1, e + [j], f + [i + j], g + [i - j])
    else:
        yield e


def solution(q):
    '''find the solution'''
    p = []
    i = 0
    for solution in findQueens(q, 0):
        for s in solution:
            p.append([i, s])
            i += 1
        print(p)
        p = []
        i = 0


solution(argN)
