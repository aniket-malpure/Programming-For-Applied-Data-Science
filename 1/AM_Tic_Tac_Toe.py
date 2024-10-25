# Mini Project 1

'''
Name: Aniket Deepak Malpure
UF ID: 61947183
Course: Programming for Applied DS (EGN5442)
Project Title: PART A-Tic-tac-toe
Project Description: In this project, we have implemented a computerized version of the game using 
                     a 2-dimensional list. This game will be played by two humans sharing the same 
                     keyboard. The screen will also show the snapshot or the state of the board after 
                     every player's move. We will store the board as a single 2-dimensional list of 
                     strings that has 3 rows and 3 columns. 
                     The program has:
                     1. Track of whose turn it is ('X' or 'O') and inform the player about it.
                     2. Allow a player to make a move. A player makes a move by informing our program 
                        at which location of the board he/she wants his/her respective symbol ('X' or 
                        'O') to be placed. The options are as follows: '0,0', '0,1', '0,2', '1,0', 
                        '1,1', '1,2', '2,0', '2,1', '2,2'. 
                     3. The player is informed the row number, followed by a comma, followed by a column 
                        number. 
                     4. The program verifies if the move is valid (for example, 3,1 is not a valid move) 
                        and, in case of an invalid move, it informs the user about it and ask for a valid 
                        move again.
                     5. Verifies if there is a winner after every player's move and also if the board is 
                        already full but we have no winners.
                     6. The program also allows the player to reinitialize the game to the beginning. 
'''

# printing the board
def printBoard(board):
    #initialing the board header
    print('-------------------------\n| R\C |  0  |  1  |  2  |\n-------------------------')
    # looping through each row and priniting the same keeping the format as given and adding dashes next line
    for row in range(3):
        print(f'|  {row}  | ', '  |  '.join(board[row]), ' |\n-------------------------')
    # printing empty line after the board
    print()

# validating user input row and column
def validateEntry(row, column, board):
    # validating of the value entered by the user is between 0 to 2 (both inclusive) for row and column
    if row < 0 or row > 2 or column < 0 or column > 2:
        print('Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.\n')
        return False
    # validating if the cell is available for user to input their entry
    elif board[row][column] != ' ':
        print('That cell is already taken.\nPlease make another selection.\n')
        return False
    # validation success response
    else:
        print('Thank you for your selection.')
        return True

# checking if the board is full and there is no more moves possible
def checkFull(board):
    # initializing a flag to check whether the board is full or not and setting it to True
    isfull = True
    # looping through each row
    for row in range(3):
        # looping through rach column within the row
        for column in range(3):
            # checking if the value at respective row and column is empty or not
            if board[row][column] == ' ':
                # if yes then setting the flag as False and breaking the loop
                isfull = False
                break
    # if the flag is True then game is over with no moves left
    if isfull:
        print('\nDRAW! NOBODY WINS!')
    return isfull

# function to determine who's turn it is to play
def checkTurn(player):
    # if last turn was X's then next will be O's
    if player == 'X':
        player = 'O'
    # if last turn was O's then next will be X's
    else:
        player = 'X'
    return player

# taking input from user where they want to play
def playerInput(player):
    # displaying whose turn it is
    print(f"{player}'s turn.")
    # asking the user to input their row and column
    print(f'Where do you want your {player} placed?')
    print('Please enter row number and column number separated by a comma.')
    # taking comma separated inputs and storing them into row and column variable
    row, column = input().split(sep=',')
    # displaying user their entered row and column
    print(f'You have entered row #{row}')
    print(f'          and column #{column}')
    return int(row), int(column)

# checking if any of the user has won the game
def checkWin(board):
    # initializing a flag iswon to False
    iswon = False
    # initializing a variable winner to identify who is the winner
    winner = 'nobody'
    # looping through row/column:
    for cell in range(3):
        # checking if we have a winner in a row (horizontally)
        if board[cell][0] != ' ' and board[cell][0] == board[cell][1] and board[cell][1] == board[cell][2]:
            winner = board[cell][0]
        # checking if we have a winner in a column (vertically)
        elif board[0][cell] != ' ' and board[0][cell] == board[1][cell] and board[1][cell] == board[2][cell]:
            winner = board[0][cell]
    # checking if we have winner diagonally
    if winner == 'nobody' and board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        winner = board[0][0]
    elif winner == 'nobody' and board[2][0] != ' ' and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        winner = board[2][0]
    # if the flag is true then display the winner
    if winner != 'nobody':
        iswon = True
        print(f'{winner} IS THE WINNER!!!')
    return iswon

# the main function through which the game is initialize
def main():
    # repeating the game until user wants to end it
    while True:
        # intializing the board
        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        # initializing the player
        player = 'O'
        # displaying that the game is started and who is going to play
        print('New Game: X goes first.\n')
        # printing the board
        printBoard(board)
        # repeating player's turn (alternate) 
        while True:
            # setting the player to play
            player = checkTurn(player)
            # taking input from user
            row, column = playerInput(player)
            # repeating above step until user enters correct input
            while True:
                # validating user's input
                if validateEntry(row, column, board):
                    # setting board value as player at user's row and column
                    board[row][column] = player
                    break
                else:
                    # incorrect user input, asking for input again
                    row, column = playerInput(player)
            # checking if there is a winner
            iswon = checkWin(board)
            if iswon:
                printBoard(board)
                break
            # checking if the board is full and there is no move possible
            isfull = checkFull(board)
            if isfull:
                printBoard(board)
                break
            printBoard(board)
        # asking user if they want to play more game?
        print('Another game? Enter Y or y for yes.')
        repeat = input()
        # if user enters other than 'Y' or 'y' then we end the game
        if repeat not in ('Y', 'y'):
            print('Thank you for playing!')
            break

if __name__ == '__main__':
    # calling the main function
    main()