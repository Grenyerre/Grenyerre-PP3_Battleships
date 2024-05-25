"""
Code Institute - Portfolio Project 3 - Battleships
Version 1.0

Legend:
'X' for placing ship and hit battleship
'O' for available space
'M' for missed shot
"""

from random import randint

"""
Construct the game boards via list comprehension
to be populated with 'X' for placed and hit battleships
"""
hidden_board = [['O'] * 8 for x in range(8)]
guess_board = [['O'] * 8 for x in range(8)]

"""
Dictionary to convert letters to numbers allows user to use
integers for row and column input
"""
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
    }


def print_board(board):
    # Print column headings and border
    print('                      A B C D E F G H')
    print('                  ---------------------')

    # Print row number and borders
    row_number = 1
    for row in board:
        print('                  |' + str(row_number) + '| ' + ' '.join(row))
        row_number += 1


def create_ships(board):
    """
    Total of 5 ships to be placed on the board,
    each generated by random row and column
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    print('\n')
    row = input(' Please enter a row for your shot, (1 - 8):\n ')
    while row not in '12345678':
        print(' Number outside of board, invalid row number.')
        row = input(' Enter a row for your shot, (1 - 8):\n ')

    print('\n')
    column = input(' Please enter a column for your shot, (A - H):\n ').upper()
    while column not in 'ABCDEFGH':
        print(' Number outside of board, invalid column letter.')
        column = input(' Enter a column for your shot, (A - H):\n ').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# Call the create_ships function to populate the hidden board
create_ships(hidden_board)


# Set the number of turns (shots) to 10
turns = 3

print('  =====================================================')
print('  ==             Welcome to Battleships              ==')
print('  =====================================================')
print('  ==         You have 5 battleships to sink          ==')
print('  ==         Your crew is depending on you!          ==')
print('  == Choose a row and a column to fire at the enemy! ==')
print('  =====================================================')
# While loop to run the game until the user has no turns left
while turns > 0:

    print('  =====================================================')
    print('                   You have ' + str(turns) + ' shots left.')
    print('  =====================================================')
    # Print hidden board for testing purposes
    # print_board(hidden_board)
    # Print guess board
    print_board(guess_board)
    row, column = get_ship_location()
    # Check if the user has already guessed the location
    if guess_board[row][column] == "M":
        print('         =========================================')
        print('         == You already guessed that location.  ==')
        print('         ==     !t was a miss! Try again.       ==')
        print('         =========================================')
    # Compare the user guess to the hidden board
    elif hidden_board[row][column] == "X":
        print('         =========================================')
        print('         ==   Good shot, you HIT a battleship!  ==')
        print('         =========================================')
        guess_board[row][column] = "X"
        turns -= 1
    else:
        print('         =========================================')
        print('         ==                MISS!                ==')
        print('         =========================================')
        guess_board[row][column] = "M"
        turns -= 1

    # If the user has hit all the battleships, end the game
    if count_hit_ships(guess_board) == 5:
        print('         =========================================')
        print('         ==          CONGRATULATIONS!           ==')
        print('         ==  You have sunk all the battleships  ==')
        print('         == You have saved your crew! Well done.==')
        print('         =========================================')
        break

    # If the user has no turns left, end the game
    if turns == 0:
        print('         =========================================')
        print('         ==          G A M E   O V E R !        ==')
        print('         ==      You have run out of shots.     ==')
        print('         ==     The enemy has won this time.    ==')
        print('         ==    BETTER LUCK NEXT TIME, CAPTAIN.  ==')
        print('         =========================================')
        break
