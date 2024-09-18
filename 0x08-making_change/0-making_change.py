#!/usr/bin/python3

""" Contains MAKE chnages function"""


def makeChange(coins, total):
    """
    Returns: less number of coins needed to get the total
        If total is 0 or less, return 0
        If total not met by any number of coins, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
