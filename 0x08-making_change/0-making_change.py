#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Determining the fewest number of coins
      needed to meet a given amount
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coinChange = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total
        coinChange += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return coinChange
