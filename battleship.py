'''One of the sample codes in codecademy'''
#import randint fn from random module
from random import randint

#create an empty list
board = []

# make the board list as 2-D list filled with Os 
for x in range(5):
    board.append(["O"] * 5)

#while printing board, remove "" and replace it with whitespace
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#fn to create a random variable
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#store the random number in a variable
ship_row = random_row(board)
ship_col = random_col(board)

#Game main code. set the number of iterations that player can play
for turn in range(4):
    print "Turn" , turn+1
    guess_row = int(raw_input("Guess Row:"))  # get user input for row
    guess_col = int(raw_input("Guess Col:"))  # get user input for column
    if guess_row == ship_row and guess_col == ship_col:  # if user input == random, break it and print game-over
        print "Congratulations! You sunk my battleship!"
        break
    else:  # failure case scenarios
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"   #set the guessed field to X (replaces O)
            print_board(board)
        if turn == 3: # final turn if user couldn’t guess the random number
            print "The ship is at row: %s column:%s! You missed it!" %(ship_row,ship_col)
print "Game Over"
