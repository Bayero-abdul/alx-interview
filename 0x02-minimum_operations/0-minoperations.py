#!/usr/bin/python3
"""A module contains a minOperation function.

"""


def minOperations(n):
    """calculates the fewest number of operations needed
     to result in exactly n H characters in the file."""

    if n <= 1:
        return 0

    target = n
    clip_board = 0
    characters = 1
    no_of_ops = 0

    while characters < target:
        if target % characters == 0:
            no_of_ops += 2
            clip_board = characters
            characters *= 2
        else:
            no_of_ops += 1
            characters += clip_board
           
    return no_of_ops
