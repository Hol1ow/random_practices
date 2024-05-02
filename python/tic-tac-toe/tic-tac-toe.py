from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("""+-------+-------+-------+
|       |       |       |
|   {value1}   |   {value2}   |   {value3}   |
|       |       |       |""".format(value1 = row[0],value2 = row[1],value3 = row[2]))
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        i = input("Enter your move: ")
        if i.isdigit():
            move = int(i)
            if move > 9 or move < 1:
                print("Invalid, try again")
                continue
            else:
                for row in board:
                    for i, s in enumerate(row):
                        if s == move:
                            row[i] = 'O'
                            return
                print("Invalid, try again")
        else:
            print("Invialid, try again")
            continue

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    result = []
    for i, row in enumerate(board):
        for idx, s in enumerate(row):
            if not (s == 'O' or s == 'X'):
                result.append((i, idx))
    print(result)
    return result


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    row = [0, 0, 0]
    column = [0, 0, 0]
    for i, s1 in enumerate(board):
        for idx, s in enumerate(s1):
            if s == sign:
                row[i] += 1
                column[idx] += 1
    win = 3 in row or 3 in column
    if not win:
        r = True
        for i in row:
            if i < 1:
                r = False
                break
        c = True
        for i in column:
            if i < 1:
                c = False
                break
        return r and c
    else:
        return win
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    slots = make_list_of_free_fields(board)
    slot = slots[randrange(len(slots))]
    board[slot[0]][slot[1]] = 'X'

board = [[1,2,3],[4,'X',6],[7,8,9]]
turn = "player"

while True:
    display_board(board)
    if (victory_for(board, 'X')):
        print("I won!")
        break
    elif (victory_for(board, 'O')):
        print("You won!")
        break
    else:
        if (turn == "player"):
            enter_move(board)
            turn = "computer"
        else:
            draw_move(board)
            turn = "player"
