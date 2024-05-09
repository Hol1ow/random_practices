def check(board: str) -> bool:
    #validation
    if not (board.isdigit() and len(board)) == 81:
        return False
    
    #population
    board_list = [[0 for i in range(9)] for i in range(9)]
    row = 0
    colum = 0
    for c in board:
        board_list[row][colum] = int(c)
        colum += 1
        if colum > 8:
            colum = 0
            row += 1

    #row check
    for r in board_list:
        for num in range(1, 10):
            if not num in r:
                return False
            
    #column check
    for i in range(9):
        c = [board_list[j][i] for j in range(9)]
        for num in range(1, 10):
            if not num in c:
                return False
            
    #sub-square check
    for c in range(0, 9, 3):
        for j in range(0, 9, 3):
            ss = board_list[c][j:j+3] + board_list[c+1][j:j+3] + \
                board_list[c+2][j:j+3]
            for num in range(1, 10):
                if not num in ss:
                    return False
                
    return True

sudoku_board1 = '295743861431865927876192543387459216612387495549216738763524189928671354154938672'
sudoku_board2 = '195743862431865927876192543387459216612387495549216738763524189928671354254938671'

print(check(sudoku_board1))
#True

print(check(sudoku_board2))
#False