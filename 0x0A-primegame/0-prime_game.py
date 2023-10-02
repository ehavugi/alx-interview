#!/usr/bin/python3
"""Prime game implementation module
"""


def count_primes(n):
    """Count primes utility func
    """
    count = 0
    if n < 2:
        return 0
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    It assumed that n and x will not be larger than 10000
    we couldn't import any packages in this task
    """

    currentPlayer = [0, 0]
    for num in nums:
        if count_primes(num) % 2 == 0:
            currentPlayer[0] += 1  # Ben wins
        else:
            currentPlayer[1] += 1  # Maria wins
    if currentPlayer[0] > currentPlayer[1]:
        return "Ben"
    elif currentPlayer[1] > currentPlayer[0]:
        return "Maria"

    return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(6, [2, 5, 1, 4, 3, 2])))
    print("Winner: {}".format(isWinner(7, [2, 5, 1, 4, 3, 2, 5])))
    print("Winner: {}".format(isWinner(6, [2, 5, 1, 4, 3, 2])))
