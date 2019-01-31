# N-Queen problem
# implemented logic - each Q in single col, backtrack when hit a dead end

def place_queens(N):
    def print_solution(board):
        for i in range(N):
            print(board[i])

    def is_Q_safe(board, Q_row, Q_col):
        # row collision
        for i in range(Q_col):
            if board[Q_row][i] == 1:
                return False

        for i, j in zip(range(Q_row, -1, -1), range(Q_col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(Q_row, N), range(Q_col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def place_Q(board, col_num):

        # escape statement
        if col_num >= N:
            return True

        # given col_num, try rows
        for i in range(N):
            if is_Q_safe(board, i, col_num):
                board[i][col_num] = 1

                # traverse True back after finding final solution
                if place_Q(board, col_num + 1):
                    return True

                # return board if all next queens were not successful
                board[i][col_num] = 0

        return False

    board = [[0 for j in range(N)] for i in range(N)]
    place_Q(board, col_num=0)
    print_solution(board)


place_queens(5)