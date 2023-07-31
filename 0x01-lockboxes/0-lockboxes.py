#!/usr/bin/python3
"""
With n number of locked boxes. Boxes are number from 0 to n-1.
each box mauy contai  keys to the other boxes.
Determine if all boxes can be opened starting form box 0
"""


def canUnlockAll(boxes):
    """
    Return True if can unlock all boxes otherwise False
    """
    n = len(boxes)
    visited = set([])
    unlocked = set([0])
    while len(unlocked) > 0:
        currentKey = unlocked.pop()
        locks = boxes[currentKey]
        visited.add(currentKey)
        if len(locks) > 0:
            for newKey in locks:
                if not(newKey in visited):
                    unlocked.add(newKey)
    if len(visited) == n:
        return True
    else:
        return False
