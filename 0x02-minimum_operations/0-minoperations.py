#!/usr/bin/python3
"""A module contains a minOperation function.

"""


def minOperations(n):
    """calculates the fewest number of operations needed
     to result in exactly n H characters in the file."""

    if n <= 1:
        return 0

    target = n
    curr_H = 1
    prev_H = 1
    ops = 0

    while curr_H < target:

        if (curr_H * 2) % 2 == 0:
            prev_H = curr_H

        if target % curr_H:
            ops += 1
            curr_H += prev_H
        else:
            ops += 2
            curr_H *= 2

    return ops
