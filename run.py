"""
Code Institute - Portfolio Project 3 - Battleships
Version 1.0

Legend:
'X' for placing ship and hit battleship
' ' for available space
'-' for missed shot
"""
from random import randint

def easy_game(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,3), randint(0,3)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
    print_board(board):
    print('   A B C D')
    print('------------')
    row_number = 1
    for row in board:
        print(" %d|%s |" % (row_number, " |".join(row)))
        row_number += 1

def medium_game(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
    print_board(board):
    print('   A B C D E F')
    print('----------------')
    row_number = 1
    for row in board:
        print(" %d|%s |" % (row_number, " |".join(row)))
        row_number += 1

def hard_game(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
    print_board(board):
    print('   A B C D E F G H')
    print('--------------------')
    row_number = 1
    for row in board:
        print(" %d|%s |" % (row_number, " |".join(row)))
        row_number += 1

# Select game difficulty level
level = input('Please select a level of difficulty: E (easy), M (medium), H (hard): ').lower()
while level not in ['E', 'M', 'H']:
    print('Invalid choice, please select a valid level of difficulty')
    level = input('Please select a level of difficulty: E (easy), M (medium), H (hard): ').lower()
    if level == 'E':
        def easy_game(board):
    elif level == 'M':
        def medium_game(board):
    else:
        def hard_game(board):


letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}       

def get_ship_location():
    row = input('Please enter a row number for your shot, between 1 and 8: ')
    while row not in '12345678':
        print('Number outside of game area, please enter a valid row number: ')
        row = input('Please enter a row number for your shot, between 1 and 8: ')
    column = input('Please enter a column letter for your shot, between A and H: ').upper()
    while column not in 'ABCDEFGH':
        print('Number outside of game area, please enter a valid column letter: ')
        column = input('Please enter a column letter for your shot, between A and H: ').upper()
    return int(row) - 1, letters_to_numbers[column]    

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count
    

create_ships(e_hidden_board, m_hidden_board, h_hidden_board)

turns = 10
while turns > 0:
    print('\nWelcome to Battleship')
    print('---------------------- ')
    print_board()
    row, column = get_ship_location()
    if e_guess_board, m_guess_board, h_guess_board[row][column] == "-":
        print('You already guessed that location, it was a miss! Try again')
    elif e_hidden_board, m_hidden_board, h_hidden_board[row][column] == "X":
        print('Good shot! You hit a battleship')
        e_guess_board, m_guess_board, h_guess_board[row][column] = "X"
        turns -= 1
    else:
        print('You missed!')
        e_guess_board, m_guess_board, h_guess_board[row][column] = "-"
        turns -= 1
    if count_hit_ships(e_guess_board, m_guess_board, h_guess_board) == 5:
        print('Congratulations! You have sunk all the battleships')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Game Over! You have run out of turns')
        break
