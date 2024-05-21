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

# Construct the game board
hidden_board = [[''] * 8 for x in range(8)]
guess_board = [[''] * 8 for x in range(8)]

"""
Dictionary to convert letters to numbers allows user to use
Integers for row and column input
"""
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(board):


def create_ships(board):


def get_ship_location():


def count_hit_ships(board):


