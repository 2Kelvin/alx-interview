#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Determining the fewest number of coins
      needed to meet a given amount
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    coinChange = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            coinChange += 1
        if (total == 0):
            return coinChange
    return -1
