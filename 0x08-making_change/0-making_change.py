#!/usr/bin/python3
""" Change comes from within"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to
    meet total .
    If total is 0 or less, return 0
    If total cannot be met by any number of
    coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total == 0:
        return num_coins
    return -1
