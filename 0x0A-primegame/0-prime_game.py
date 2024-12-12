#!/usr/bin/python3
"""
Module defines a function for prime game.
"""


def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Precompute prime counts up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the total primes up to n
        total_primes = prime_count[n]

        # If total primes is odd, Maria wins (Maria starts first)
        # If even, Ben wins
        if total_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
