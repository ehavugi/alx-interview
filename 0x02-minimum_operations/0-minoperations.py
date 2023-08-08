#!/usr/bin/python3
"""
With Copy all and paste operation.Given a number
n, the module function minOperations(n) returns
or calculates the fewest number of operations need to result in
excactly n H characters in the file.
"""


def minOperations(n):
    """
    Least Common Divisors are found and added up except 1
    n = 0, we found impossible as we don't have delete
    n = 1, we found we can return without operations.
    other operations are set as sum of Least common divisions
    with repeation.
    """
    ops = 0
    if n == 0 or (n//1 != n):
        return 0
    if n == 1:
        return 0
    i = 2
    while n > 1 and i <= n:
        if n % i == 0:
            n = n//i
            ops += i
        else:
            i = i + 1
    return ops
