"""
Code Institute - Portfolio Project 3 - Battleships
Version 1.0

Legend:
'X' for placing ship and hit battleship
'O' for available space
'M' for missed shot
"""

# import colorama
# from colorama import Fore, Back, Style
from random import randint

"""
Construct the game boards via list comprehension
to be populated with 'X' for placed and hit battleship
"""
hidden_board = [['O'] * 8 for x in range(8)]
guess_board = [['O'] * 8 for x in range(8)]

"""
Dictionary to convert letters to numbers allows user to use
Integers for row and column input
"""
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):
    # Print column headings and border
    print('  A B C D E F G H')
    print('------------------')

    # Print row number and borders
    row_number = 1
    for row in board:
        print(str(row_number) + '|' + ' '.join(row) + '|')
        row_number += 1

def create_ships(board):
    """
    Total of 5 ships to be placed on the board,
    each generated by random row and column
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"  

def get_ship_location():
    row = input('  Please enter a row number for your shot, between 1 and 8: ')
    while row not in '12345678':
        print('  Number outside of board, please enter a valid row number (1 - 8): ')
        row = input('  Please enter a row number for your shot, between 1 and 8: ')
    
    column = input('  Please enter a column letter for your shot, between A and H: ').upper()
    while column not in 'ABCDEFGH':
        print('  Number outside of board, please enter a valid column letter (A - H): ')
        column = input('  Please enter a column letter for your shot, between A and H: ').upper()
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

# Set the number of turns to 10
turns = 10
# While loop to run the game until the user has no turns left
while turns > 0:
    print('  ==============================')
    print('  ==  Welcome to Battleships  ==')
    print('  ==============================')
    print_board(hidden_board)
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == "M":
        print('You already guessed that location, it was a miss! Try again')
    elif hidden_board[row][column] == "X":
        print('Good shot! You hit a battleship')
        guess_board[row][column] = "X"
        turns -= 1
    else:
        print('You missed!')
        guess_board[row][column] = "M"
        turns -= 1
    if count_hit_ships(guess_board) == 5:
        print('Congratulations! You have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Game Over! You have run out of turns')
        break

