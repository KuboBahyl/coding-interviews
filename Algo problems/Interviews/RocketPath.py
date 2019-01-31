# Input: M x N grid of positive integers
grid = [
    [3, 6, 4],
    [8, 4, 9],
    [9, 1, 1],
    [5, 0, 5],
    [1, 2, 3]
]
"""
rocket starts in the first row
every cell of the grid contains a positive integer
every step it can go straight up, up-left, up-right
can’t leave the grid
Output: What’s the maximum total sum of collected numbers?
Out -> 30
Out2 -> path
"""

# try every path: worst 3^M
# row after row, write possible sums: M*N

import copy


def max_rocket_sum(grid):
    M = len(grid)
    if M == 0:
        return

    N = len(grid[0])
    if N == 0:
        return

    # M,N > 0
    cost_grid = copy.deepcopy(grid)
    for i in range(1, M):
        for j in range(N):
            if j == 0:
                cost_grid[i][j] += max(cost_grid[i - 1][j], cost_grid[i - 1][j + 1])
            elif j == N - 1:
                cost_grid[i][j] += max(cost_grid[i - 1][j - 1], cost_grid[i - 1][j])
            else:
                cost_grid[i][j] += max(cost_grid[i - 1][j - 1], cost_grid[i - 1][j], cost_grid[i - 1][j + 1])

    # find max
    max_cost = 0
    for j in range(N):
        if cost_grid[-1][j] > max_cost:
            max_cost = cost_grid[-1][j]
            last_j = j

    best_path = [None] * M
    best_path[-1] = grid[-1][last_j]
    for i in range(M - 2, -1, -1):
        max_j = last_j
        for j in range(N):
            if last_j - 1 <= j <= last_j + 1:
                val = cost_grid[i][j]
                if val > cost_grid[i][max_j]:
                    max_j = j

        best_path[i] = grid[i][max_j]
        last_j = max_j

    return max_cost, best_path


max_rocket_sum(grid)