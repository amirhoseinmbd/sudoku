def is_valid(board, row, col, num):
    
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:  
            return False
 
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def amir_solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  
                for num in range(1, 10): 
                    if is_valid(board, row, col, num):
                        board[row][col] = num  

                        if amir_solve(board):  
                            return True
                        else:
                            board[row][col] = 0  
                return False
    return True


def print_board(board):
    for row in board:
        print(' '.join(str(num) for num in row))


board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 3, 5, 0, 0, 8, 9, 0],
    [0, 2, 0, 8, 0, 9, 6, 0, 0],
    [0, 9, 0, 0, 1, 0, 0, 0, 3],
    [0, 0, 4, 0, 0, 5, 0, 0, 0],
    [3, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 5, 2, 0, 9, 0, 3, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 1, 0, 0, 0]
]

if amir_solve(board):
    print_board(board)
else:
    print('There is no solution!')
