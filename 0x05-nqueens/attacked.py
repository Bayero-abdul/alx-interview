#!/usr/bin/python3

from typing import List

def attacked(row: int, col: int, n: int) -> List[List]:
    """Returns a list of attacked boxes in a chess board
    by a queen
    """
    boxes = []

	#horizontal
    for new_col in range(col-1, -1, -1):
        boxes.append([row, new_col])
    for new_col in range(col+1, n):
        boxes.append([row, new_col])

	#vertical
    for new_row in range(row-1, -1, -1):
        boxes.append([new_row, col])
    for new_row in range(row+1, n):
        boxes.append([new_row, col])

	#diagonal
    for i in range(1, n):
        if row + i < n and col + i < n:
            boxes.append([row+i, col+i])
        if row - i >= 0 and col - i >= 0:
            boxes.append([row-i, col-i])


        if row + i < n and col - i >= 0:
            boxes.append([row+i, col-i])
        if row - i >= 0 and col + i < n:
            boxes.append([row-i, col+i])

    return boxes
