#!/usr/bin/python3
'''N Queens'''
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N\n')
    sys.exit(1)
elif type(sys.argv[1]) != int:
    print('N must be a number\n')
    sys.exit(1)
elif sys.argv[1] < 4:
    print('N must be atleast 4\n')
    sys.exit(1)
else:
    # solution here
    pass