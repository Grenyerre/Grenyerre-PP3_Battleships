"""
Code Institute - Portfolio Project 3 - Battleships
Version 1.0

Legend:
'X' for placing ship and hit battleship
' ' for available space
'-' for missed shot
"""
from random import randint
from colorama import Fore, Back, Style

"""
Construct the game boards via list comprehension
to be populated with 'X' for placing ship and hit battleship
"""
hidden_board = [[''] * 8 for x in range(8)]
guess_board = [[''] * 8 for x in range(8)]

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


def get_ship_location():


def count_hit_ships(board):


