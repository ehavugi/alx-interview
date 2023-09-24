#!/usr/bin/python3
"""
return smallest number of change possible.
if not possible return -1
if the total is 0 or less return 0

"""


def makeChange(coins, total):
    """Given a list of coins and totalm return min number of
    coins needed for change
    """
    if total <= 0:
        return -1
    dictD = {}
    for coin in coins:
        dictD[coin] = (total % coin)

    Set = False
    extra = 0
    for value in dictD.values():
        if value == 0:
            Set = True
        else:
            extra += value
    if not Set and total % extra != 0:
        return -1
    changeUpTo = [float('inf')] * (total + 1)
    changeUpTo[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i-coin >= 0:
                changeUpTo[i] = min(changeUpTo[i], changeUpTo[i - coin] + 1)
    if changeUpTo[total] == float('inf'):
        return -1
    return changeUpTo[total]
