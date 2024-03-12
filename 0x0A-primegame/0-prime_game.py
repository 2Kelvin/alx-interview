#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """find the winner"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    e = [1 for r in range(sorted(nums)[-1] + 1)]
    e[0], e[1] = 0, 0
    for h in range(2, len(e)):
        primeX(e, h)

    for h in nums:
        if sum(e[0:h + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def primeX(ls, x):
    """primez function"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
