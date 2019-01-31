# Largest connected component in a grid
grid = [
    [1, 2, 2, 2],
    [1, 3, 3, 2],
    [1, 3, 2, 2],
]


# out: 5


def largest_component(grid):
    def can_move(i, j, visited, value):
        if i < 0 or i > M - 1:
            return False
        if j < 0 or j > N - 1:
            return False
        if visited[i][j]:
            return False
        if grid[i][j] != value:
            return False
        return True

    def search(i, j, visited, area=1):
        visited[i][j] = True
        value = grid[i][j]

        if can_move(i - 1, j, visited, value):
            area, visited = search(i - 1, j, visited, area + 1)
        if can_move(i, j + 1, visited, value):
            area, visited = search(i, j + 1, visited, area + 1)
        if can_move(i + 1, j, visited, value):
            area, visited = search(i + 1, j, visited, area + 1)
        if can_move(i, j - 1, visited, value):
            area, visited = search(i, j - 1, visited, area + 1)

        return area, visited

    M = len(grid)
    if M == 0:
        return 0

    N = len(grid[0])
    if N == 0:
        return 0

    # M, N > 0
    visited = [[False] * N for x in range(M)]
    max_area = 0

    for i in range(M):
        for j in range(N):
            if not visited[i][j]:
                area, visited = search(i, j, visited)
                if area > max_area:
                    max_area = area

    return max_area


largest_component(grid)
# Time: O(M*N)
# Space: O(M*N)
# brute force would give at worst O((M*N)^(M*N-1)) time and O(1) space