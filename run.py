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