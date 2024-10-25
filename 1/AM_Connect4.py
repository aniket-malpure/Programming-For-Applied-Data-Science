# Mini Project 1

'''
Name: Aniket Deepak Malpure
UF ID: 61947183
Course: Programming for Applied DS (EGN5442)
Project Title: PART B - Connect four
Project Description: Connect 4 is a game in which the players choose a symbol and then take turns 
                    dropping colored tokens into a six-row, seven-column vertically suspended grid. 
                    The game is developed with the help of classes and objects:
                    1. class Board: This class has method to print the board
                    2. class Game: This class has the method which will be required while playing 
                                   the game such as checkTurn, playerInput, validateEntry, checkWin,
                                   checkFull, play.
                    The main function initiated the game by creating object of class Game and once the
                    game is over it asks user to continue playing another game or not.
'''

# class to define the board and display it
class Board:

    # init function to intialize empty board
    def __init__(self):
        # empty board
        self.grid = [[' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ']]
        # initializing the available position to play
        self.availablePlaces = ['a1','b1','c1','d1','e1','f1','g1']
        # assigning numerical value to alphabet to access the column in 2D matrix
        self.alphabetToNumber = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6}

    # printing the board
    def printBoard(self):
        # looping through each row and priniting the same keeping the format as given and adding dashes next line
        for row in range(5, -1, -1):
            print(f'|  {row+1}  | ', '  |  '.join(self.grid[row]), ' |\n-------------------------------------------------')
        # printing empty line after the board
        print('| R/C |  a  |  b  |  c  |  d  |  e  |  f  |  g  |\n-------------------------------------------------\n')

class Game:

    # init function to intialize empty board
    def __init__(self):
        self.board = Board()
        self.player = 'O'

    # function to determine who's turn it is to play
    def checkTurn(self):
        # if last turn was X's then next will be O's
        if self.player == 'X':
            self.player = 'O'
        # if last turn was O's then next will be X's
        else:
            self.player = 'X'
        return self.player

    # taking input from user where they want to play
    def playerInput(self):
        # displaying whose turn it is
        print(f"{self.player}'s turn.")
        # asking the user to input their row and column
        print(f'Where do you want your {self.player} placed?')
        # displaying available choices
        print(f'Available positions are: {self.board.availablePlaces}')
        # taking comma separated inputs and storing them into row and column variable
        userInput = input("Please enter column-letter and row-number (e.g., a1): ")
        return userInput

    # validating user input row and column
    def validateEntry(self, userInput):
        # checking if user entered input is present in our available choices list
        if userInput not in self.board.availablePlaces:
            print('Please enter correct input from the available options.')
            return False
        else:
            print('Thank you for your selection.')
            return True

    # updating the board as the user inputs their selection
    def updateBoard(self, userInput):
        # updating user entered row and column combination with player symbol
        row = int(userInput[1])-1
        column = int(self.board.alphabetToNumber[userInput[0]])
        self.board.grid[row][column] = self.player
        # updating available places
        if row < 5:
            self.board.availablePlaces = [element if element != userInput else userInput[0] + str(row+2) for element in self.board.availablePlaces]
            #self.board.availablePlaces[column] = userInput[0] + str(row+2)
        else:
            self.board.availablePlaces.remove(userInput)

    # checking if any of the user has won the game
    def checkWin(self, userInput):
        # row index
        row = int(userInput[1])-1
        # column index
        col = int(self.board.alphabetToNumber[userInput[0]])
        # All the possible directions in which we have to check winning position
        directions = [(0,1), (1,0), (1,1), (-1, 1)]
        # (0,1): In a row (Horizontally)
        # (1,0): In a column (Vertically)
        # (1,1): Towards up right and down left (Diagonally)
        # (-1,1): Towards up left and down right (Diagonally)
        for dir in directions:
            # row and column incremental values
            r = dir[0]
            c = dir[1]
            # initializing count variable to get count of consecutive same elements
            count = 1
            # temp variable to initialize row and column so that we can update these temp variables
            rowIncremental = row
            colIncremental = col
            # checking within constraints of the board whether the next element is matching the current by adding r and c
            while (rowIncremental+r < 6 and rowIncremental+r >= 0 and colIncremental+c < 7 and colIncremental+c >= 0
                   and self.board.grid[rowIncremental+r][colIncremental+c] == self.player):
                count+=1
                rowIncremental+=r
                colIncremental+=c
            # temp variable to initialize row and column so that we can update these temp variables
            rowIncremental = row
            colIncremental = col
            # checking within constraints of the board whether the next element is matching the current by subtracting r and c
            while (rowIncremental-r < 6 and rowIncremental-r >= 0 and colIncremental-c < 7 and colIncremental-c >= 0 
                   and self.board.grid[rowIncremental-r][colIncremental-c] == self.player):
                count+=1
                rowIncremental-=r
                colIncremental-=c
            # checking of the count is greater than or equal to 4 to identify the winner
            if count >= 4:
                print(f'{self.player} IS THE WINNER!!!')
                return True
        return False
    
    # checking if the board is full and there is no more moves possible
    def checkFull(self):
        # initializing a flag to check whether the board is full or not and setting it to True
        isfull = True
        # looping through each row
        for row in range(6):
            # looping through rach column within the row
            for column in range(7):
                # checking if the value at respective row and column is empty or not
                if self.board.grid[row][column] == ' ':
                    # if yes then setting the flag as False and breaking the loop
                    isfull = False
                    break
        # if the flag is True then game is over with no moves left
        if isfull:
            print('\nDRAW! NOBODY WINS!')
        return isfull
    
    # function to initiate the game
    def play(self):
        # displaying that the game is started and who is going to play
        print("New game: X goes first.\n")
        # printing the board
        self.board.printBoard()
        # repeating player's turn (alternate) 
        while True:
            # setting the player to play
            self.player = self.checkTurn()
            # taking input from user
            userInput = self.playerInput()
            # repeating above step until user enters correct input
            while True:
                # validating user's input
                if self.validateEntry(userInput):
                    # setting board value as player at user's row and column
                    self.updateBoard(userInput)
                    break
                else:
                    # incorrect user input, asking for input again
                    userInput = self.playerInput()
            # checking if there is a winner
            iswon = self.checkWin(userInput)
            if iswon:
                self.board.printBoard()
                break
            # checking if the board is full and there is no move possible
            isfull = self.checkFull()
            if isfull:
                self.board.printBoard()
                break
            # printing the board
            self.board.printBoard()

# the main function through which the game is initialize
def main():
    # repeating the game until user wants to end it
    while True:
        # initializing a new game
        game = Game()
        game.play()
        # asking user if they want to play more game?
        repeat = input('Another game (y/n)? ')
        # if user enters other than 'Y' or 'y' then we end the game
        if repeat not in ('Y', 'y'):
            print('Thank you for playing!')
            break

if __name__ == '__main__':
    # calling the main function
    main()