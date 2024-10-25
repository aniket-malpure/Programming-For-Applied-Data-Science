"""
Tic-Tac-Toe
This program is a simple Tic-Tac-Toe game using classes and objects.
Additionally a human can play this program with a computer.
"""

# importing pickle and numpy model
import pickle
import numpy as np
import sklearn
import pandas as pd

# accessing the ML model 
with open(r'C:\Study\MS\Programming for Data Science\Coding Assignments\Mini Project\2\model.pkl', 'rb') as file:
    model = pickle.load(file)

# define Board class to building the Game Board:
class Board:

    # this constructor initiates the board with empty cells
    def __init__(self):
        self.c = [[" "," "," "],
                  [" "," "," "],
                  [" "," "," "]]
        
    # this method prints the board. Recall that class methods are functions
    def printBoard(self):
        # it first prints the BOARD_HEADER constant
        # BOARD_HEADER constant
        BOARD_HEADER = "-------------------------\n| R\C |  0  |  1  |  2  |\n-------------------------"
        print(BOARD_HEADER)
        # looping through each row and priniting the same keeping the format as given and adding dashes next line
        for row in range(3):
            print(f'|  {row}  | ', '  |  '.join(self.c[row]), ' |\n-------------------------')
        # printing empty line after the board
        print()

# define Game class to implement the Game Logic:
class Game:

    # the constructor
    def __init__(self):
        self.board = Board()
        self.turn = 'X'

    # this method switches players
    def switchPlayer(self):
        # if last turn was X's then next will be O's
        if self.turn == 'X':
            self.turn = 'O'
        # if last turn was O's then next will be X's
        else:
            self.turn = 'X' 

    # this method validates the user's entry
    def validateEntry(self, row, col):
        # validating of the value entered by the user is between 0 to 2 (both inclusive) for row and column
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.\n')
            return False
        # validating if the cell is available for user to input their entry
        elif self.board.c[row][col] != ' ':
            print('That cell is already taken.\nPlease make another selection.\n')
            return False
        # validation success response
        else:
            print('Thank you for your selection.')
            return True

    # this method checks if the board is full
    def checkFull(self):
        # initializing a flag to check whether the board is full or not and setting it to True
        isfull = True
        # looping through each row
        for row in range(3):
            # looping through rach column within the row
            for column in range(3):
                # checking if the value at respective row and column is empty or not
                if self.board.c[row][column] == ' ':
                    # if yes then setting the flag as False and breaking the loop
                    isfull = False
                    break
        # if the flag is True then game is over with no moves left
        if isfull:
            print('\nDRAW! NOBODY WINS!')
        return isfull

    # this method checks for a winner
    def checkWin(self):
        # initializing a flag iswon to False
        iswon = False
        # initializing a variable winner to identify who is the winner
        winner = 'nobody'
        # looping through row/column:
        for cell in range(3):
            # checking if we have a winner in a row (horizontally)
            if self.board.c[cell][0] != ' ' and self.board.c[cell][0] == self.board.c[cell][1] and self.board.c[cell][1] == self.board.c[cell][2]:
                winner = self.board.c[cell][0]
            # checking if we have a winner in a column (vertically)
            elif self.board.c[0][cell] != ' ' and self.board.c[0][cell] == self.board.c[1][cell] and self.board.c[1][cell] == self.board.c[2][cell]:
                winner = self.board.c[0][cell]
        # checking if we have winner diagonally
        if winner == 'nobody' and self.board.c[0][0] != ' ' and self.board.c[0][0] == self.board.c[1][1] and self.board.c[1][1] == self.board.c[2][2]:
            winner = self.board.c[0][0]
        elif winner == 'nobody' and self.board.c[2][0] != ' ' and self.board.c[2][0] == self.board.c[1][1] and self.board.c[1][1] == self.board.c[0][2]:
            winner = self.board.c[2][0]
        # if the flag is true then display the winner
        if winner != 'nobody':
            iswon = True
            print(f'{winner} IS THE WINNER!!!')
        return iswon
    
    # this method checks if the game has met an end condition by calling checkFull() and checkWin()
    def checkEnd(self):
        # checking if there is a winner
        iswon = self.checkWin()
        # checking if the board is full and there is no move possible
        isfull = self.checkFull()
        self.board.printBoard()
        # if either is true then return true
        if iswon or isfull:
            return True

    # taking input from user where they want to play
    def playerInput(self):
        # displaying whose turn it is
        print(f"{self.turn}'s turn.")
        # asking the user to input their row and column
        print(f'Where do you want your {self.turn} placed?')
        print('Please enter row number and column number separated by a comma.')
        # taking comma separated inputs and storing them into row and column variable
        # if human is the player then we take input
        if self.turn == 'X':
            row, col = input().split(sep=',')
        # if it is computer then we produce an output from our ML model
        else:
            # a list to store current board status
            inp = []
            for i in range(3):
                for j in range(3):
                    # if X on the cell then append 1 to the list
                    if self.board.c[i][j] == 'X':
                        inp.append(1)
                    # if 0 on the cell then append -1 to the list
                    elif self.board.c[i][j] == 'O':
                        inp.append(-1)
                    # if the cell is empty then append 0 to the list
                    else:
                        inp.append(0)
            # converting the list to a 2D list
            inp = [inp]
            # converting 2D list to a dataframe
            modelInput = pd.DataFrame(inp, columns=['x0','x1', 'x2','x3','x4','x5','x6','x7','x8'])
            # predicting the output optimal position based on our ML model
            output = int(model.predict(modelInput))
            # deriving row and column based on the output
            row = output // 3
            col = output % 3
        # displaying user their entered row and column
        print(f'You have entered row #{row}')
        print(f'          and column #{col}')
        return int(row), int(col)

    # this method runs the tic-tac-toe game
    def playGame(self):
        # repeating player's turn (alternate) 
        while True:
            # taking input from user
            row, column = self.playerInput()
            # repeating above step until user enters correct input
            while True:
                # validating user's input
                if self.validateEntry(row, column):
                    # setting board value as player at user's row and column
                    self.board.c[row][column] = self.turn
                    break
                else:
                    # incorrect user input, asking for input again
                    row, column = self.playerInput()
            # checking if the game is ended
            if self.checkEnd():
                break
            # switching the user
            self.switchPlayer()

# main function
def main():
    # using while-loop that runs until the user says no for another game
    while True:
        # first initializes a variable to repeat the game
        game = Game()
        # displaying that the game is started and who is going to play
        print('New Game: X goes first.\n')
        # printing the board
        game.board.printBoard()
        # start the game
        game.playGame()
        # asking user if they want to play more game?
        print('Another game? Enter Y or y for yes.')
        repeat = input()
        # if user enters other than 'Y' or 'y' then we end the game
        if repeat not in ('Y', 'y'):
            print('Thank you for playing!')
            break

# call to main() function
if __name__ == "__main__":
    main()
