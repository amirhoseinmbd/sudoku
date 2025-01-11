def is_valid(board, row, col, num):
    
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:  
            return False
         
    if row <= 2 :
        start_row = 0
    elif 2 < row <=5 :
        start_row = 3
    else :
        start_row = 6

    if col <= 2 :
        start_col = 0
    elif 2 < col <=5 :
        start_col = 3
    else :
        start_col = 6

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
    print('ey vayyyy')
