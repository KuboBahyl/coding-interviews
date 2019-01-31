# N-Queen problem
# implemented logic - place Q col after col, hold occupied rows and diagonals in memory
# in other words - decide in O(1) whether to continue just before testing it O(n)

def place_queens_BB(N):
    def print_solution(board):
        for row in board:
            print(row)

    def is_Q_safe(Q_row, Q_col, used_row, used_slash, used_backslash):
        if used_row[Q_row]:
            return False

        if used_slash[slash_board[Q_row][Q_col]]:
            return False

        if used_backslash[backslash_board[Q_row][Q_col]]:
            return False

        return True

    def place_Q(used_row=[False] * N, used_slash=[False] * (2 * N + 1), used_backslash=[False] * (2 * N + 1),
                col_num=0):

        # solution escape statement
        if col_num > N - 1:
            return True

        # iteratin over rows
        for i in range(N):
            # check the queen safety
            if is_Q_safe(i, col_num, used_row, used_slash, used_backslash):

                # update arrays
                board[i][col_num] = 1
                used_row[i] = True
                used_slash[slash_board[i][col_num]] = True
                used_backslash[backslash_board[i][col_num]] = True

                # recursively place next Q
                if place_Q(used_row, used_slash, used_backslash, col_num + 1):
                    return True

                # if another place_Q fails, return the table to normal
                board[i][col_num] = 0
                used_row[i] = False
                used_slash[slash_board[i][col_num]] = False
                used_backslash[backslash_board[i][col_num]] = False

        # if all possibilities were testes and nothing passed, return False
        return False

    board = [[0 for j in range(N)] for i in range(N)]
    slash_board = [[i + j for j in range(N)] for i in range(N)]
    backslash_board = [[i - j + N - 1 for j in range(N)] for i in range(N)]

    place_Q()

    print_solution(board)


place_queens_BB(8)