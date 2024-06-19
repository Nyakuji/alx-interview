#!/usr/bin/python3
""" Change comes from within"""


def makeChange(coins, total):
    if total < 0:
        return -1
    if total == 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each
    # total
    min_coins = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    min_coins[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins needed for each total
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # If the minimum number of coins for the total is still infinity, it means
    # the total cannot be met
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
