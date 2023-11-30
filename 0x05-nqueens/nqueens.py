#!/usr/bin/python3


from typing import List
from attacked import attacked



def dfs(solution, i, j, n, attacked_boxes=[]):
    solution.append([i, j])
    attacked_boxes = attacked_boxes + attacked(i, j, n)
    attacked_boxes.append([i, j])
    
    col = j
    for row in range(i, n):
        while col < n:
            if [row, col] not in attacked_boxes:
                return dfs(solution, row, col, n, attacked_boxes)
            col += 1
        if col >= n:
            col = 0
    
    return solution


def nqueens(n: int) -> List[List]:
    for i in range(n):
        for j in range(n):
            solution = []
            x = dfs(solution, i, j , n)
            print("x -> ",x)
            if len(x) == n:
                print(x)
