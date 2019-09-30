
import random
from messages import (
    TTT_SUCCESS_MESSAGE, TTT_ERROR_MESSAGES)

def draw_the_board(board):
    print('-------------')
    print('|' +' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('-------------')
    print('|' +' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('-------------')
    print('|' +' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    #   print('|          |')
    print('-------------')

def choose_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(TTT_SUCCESS_MESSAGE["choose_letter"])
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def who_plays_first():
    return 'computer'

def play_again():
    print(TTT_SUCCESS_MESSAGE["play_again"])
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(board, letter):
    bo = board
    le = letter
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or
        (bo[4] == le and bo[5] == le and bo[6] == le) or
        (bo[1] == le and bo[2] == le and bo[3] == le) or
        (bo[7] == le and bo[4] == le and bo[1] == le) or
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def get_board_copy(board):
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board

def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    if board[move] == ' ':
        return True
    return False

def get_player_move(board):
    move = ' '
    if move not in '1 2 3 4 5 6 7 8 9'.split():
        print(TTT_SUCCESS_MESSAGE["enter_move"])
        move = input()
    if not is_space_free(board, int(move)):
        print(TTT_ERROR_MESSAGES["space_occupied"])
        move = input()
    # game_is_playing = False
    return int(move)

def choose_random_move(board, moves_list):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move(board, [2, 4, 6, 8])

def check_if_board_is_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

print(TTT_SUCCESS_MESSAGE["welcome_message"])

while True:
    # Reset the board
    the_board = [' '] * 10
    player_letter, computer_letter = choose_player_letter()
    turn = who_plays_first()
    print(TTT_SUCCESS_MESSAGE["play_first"].format(turn))
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's turn.
            draw_the_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_the_board(the_board)
                print(TTT_SUCCESS_MESSAGE["player_win"])
                game_is_playing = False
            else:
                if check_if_board_is_full(the_board):
                    draw_the_board(the_board)
                    print(TTT_SUCCESS_MESSAGE["draw"])
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn.
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_the_board(the_board)
                print(TTT_SUCCESS_MESSAGE["computer_win"])
                game_is_playing = False
            else:
                if check_if_board_is_full(the_board):
                    draw_the_board(the_board)
                    print(TTT_SUCCESS_MESSAGE["draw"])
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
