#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of
coin in the list
Your solution’s runtime will be evaluated in this task
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount
    total.

    Args:
        coins (list): List of the values of the coins in possession.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not
             possible.
    """
    if total <= 0:
        return 0

    # Initialize a DP array with a value greater than the maximum
    # possible coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Build up the DP table
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot
    # be met
    return dp[total] if dp[total] != float('inf') else -1
