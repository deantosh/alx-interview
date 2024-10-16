#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste. Given
a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

 - Prototype: def minOperations(n)
 - Returns an integer
 - If n is impossible to achieve, return 0
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    # Start with the smallest factor 2 up to n
    for i in range(2, n + 1):
        while n % i == 0:  # Check if i is a factor of n
            operations += i  # Copy and paste operations
            n //= i  # Reduce n
    return operations
