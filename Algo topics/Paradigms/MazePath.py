# Rat in Maze problem - given maze, find path from [0,0] to [N-1, N-1]
# moving only down and right
# not possible to just rewrite maze
maze = [[1, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]


# output=[ [1, 0, 0, 0],
#          [1, 1, 0, 0],
#          [0, 1, 0, 0],
#          [1, 1, 1, 1] ]

def find_path_in_maze(maze, N):
    def solve_maze(maze, N, pos_row, pos_col, maze_out):
        # one and only True return statement
        if pos_row == N - 1 and pos_col == N - 1:
            return True

        # do this at each cell
        if go_right(maze, N, pos_row, pos_col):
            pos_col += 1
            maze_out[pos_row][pos_col] = 1
            if solve_maze(maze, N, pos_row, pos_col, maze_out) == True:
                return True

        if go_down(maze, N, pos_row, pos_col):
            pos_row += 1
            maze_out[pos_row][pos_col] = 1
            return solve_maze(maze, N, pos_row, pos_col, maze_out)

        else:
            maze_out[pos_row][pos_col] = 0
            return False

    def go_right(maze, N, pos_row, pos_col):
        return pos_col < N - 1 and maze[pos_row][pos_col + 1] == 1

    def go_down(maze, N, pos_row, pos_col):
        return pos_row < N - 1 and maze[pos_row + 1][pos_col] == 1

    def print_solution(maze, N):
        for i in range(N):
            print(maze[i])

    N = len(maze)
    begin_row = begin_col = 0

    maze_out = [[0 for j in range(N)] for i in range(N)]
    maze_out[0][0] = 1

    if solve_maze(maze, N, begin_row, begin_col, maze_out) == False:
        print("Solution does not exist")
    else:
        print_solution(maze_out, N)


find_path_in_maze(maze, 4)