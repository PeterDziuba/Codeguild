import os
import random
import time

class Board:
    def __init__(self, b_list):
        self.b_list = b_list

    def print_board(self):
        print("")
        print(' 1   2   3   4   5   6   7')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(
              self.b_list[0][0], self.b_list[0][1], 
              self.b_list[0][2], self.b_list[0][3], self.b_list[0][4],
              self.b_list[0][5], self.b_list[0][6]))
        print('____________________________')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(self.b_list[1][0],
              self.b_list[1][1], self.b_list[1][2], self.b_list[1][3], self.b_list[1][4],
              self.b_list[1][5], self.b_list[1][6]))
        print('____________________________')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(self.b_list[2][0],
          self.b_list[2][1], self.b_list[2][2], self.b_list[2][3], self.b_list[2][4],
          self.b_list[2][5], self.b_list[2][6]))
        print('____________________________')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(self.b_list[3][0],
          self.b_list[3][1], self.b_list[3][2], self.b_list[3][3], self.b_list[3][4],
          self.b_list[3][5], self.b_list[3][6]))
        print('____________________________')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(self.b_list[4][0],
              self.b_list[4][1], self.b_list[4][2], self.b_list[4][3], self.b_list[4][4],
              self.b_list[4][5], self.b_list[4][6]))
        print('____________________________')
        print(' {} | {} | {} | {} | {} | {} | {}'.format(self.b_list[5][0],
              self.b_list[5][1], self.b_list[5][2], self.b_list[5][3], self.b_list[5][4],
              self.b_list[5][5], self.b_list[5][6]))
        print('____________________________')

    def is_winner(self, player_one, player_two):
        # check horizontal spaces
        for x in range(6):
            for y in range(3):
                if ((self.b_list[x][y] == player_one) and
                   (self.b_list[x][y+1] == player_one) and
                   (self.b_list[x][y+2] == player_one) and
                   (self.b_list[x][y+3] == player_one)):
                    print('Player One Wins!')
                    return True
                elif ((self.b_list[x][y] == player_two) and
                 (self.b_list[x][y+1] == player_two) and
                 (self.b_list[x][y+2] == player_two) and
                 (self.b_list[x][y+3] == player_two)):
                    print('Player Two Wins!')
                    return True

        # check vertical spaces
        for x in range(3):
            for y in range(7):
                if ((self.b_list[x][y] == player_one) and
                   (self.b_list[x+1][y] == player_one) and
                   (self.b_list[x+2][y] == player_one) and
                   (self.b_list[x+3][y] == player_one)):
                    print('Player One Wins!')
                    return True
                elif ((self.b_list[x][y] == player_two) and
                   (self.b_list[x+1][y] == player_two) and
                   (self.b_list[x+2][y] == player_two) and
                   (self.b_list[x+3][y] == player_two)):
                    print('Player Two Wins!')
                    return True

        # check / diagonal spaces
        for x in range(3, 6):
            for y in range(4):
                if ((self.b_list[x][y] == player_one) and
                   (self.b_list[x-1][y+1] == player_one) and
                   (self.b_list[x-2][y+2] == player_one) and
                   (self.b_list[x-3][y+3] == player_one)):
                    print('Player One Wins!')
                    return True
                elif ((self.b_list[x][y] == player_two) and
                   (self.b_list[x-1][y+1] == player_two) and
                   (self.b_list[x-2][y+2] == player_two) and
                   (self.b_list[x-3][y+3] == player_two)):
                    print('Player Two Wins!')
                    return True

        # check \ diagonal spaces
        for x in range(3):
            for y in range(4):
                if ((self.b_list[x][y] == player_one) and
                 (self.b_list[x+1][y+1] == player_one) and
                 (self.b_list[x+2][y+2] == player_one) and
                 (self.b_list[x+3][y+3] == player_one)):
                    print('Player One Wins!')
                    return True
                elif ((self.b_list[x][y] == player_two) and
                 (self.b_list[x+1][y+1] == player_two) and
                 (self.b_list[x+2][y+2] == player_two) and
                 (self.b_list[x+3][y+3] == player_two)):
                    print('Player Two Wins!')
                    return True

        return False

    def check_position(self, user_position):
        x = 5
        while x > -1:
            if self.b_list[x][user_position] == ' ':
                position = [x, user_position]
                return position
            else: x -= 1
        print('You aren\'t allowed to play there!')


def get_position():
    user_position = int(input('Where would you like to play?\n(1-7): '))
    return (user_position-1)    

def what_token_to_play(whose_turn, player_one, player_two):
    if not whose_turn:
        play = player_one
    else:
        play = player_two
    return play

def whose_turn_is_it(whose_turn):
    if whose_turn:
        whose_turn -= 1
    elif not whose_turn:
        whose_turn += 1
    return whose_turn

def player_turn_banner(whose_turn):
    if whose_turn:
        print("Player Two's Turn:")
        print('')
    elif not whose_turn:
        print("Player One's Turn:")
        print('')

def play_with_people(board, player_one, player_two, whose_turn):
    control_loop = True
    while not board.is_winner(player_one, player_two):
        os.system('clear')
        board.print_board()
        player_turn_banner(whose_turn)
        column_pos = get_position()
        position = board.check_position(column_pos)
        my_row = position[0]
        my_column = position[1]
        play = what_token_to_play(whose_turn, player_one, player_two)
        board.b_list[my_row][my_column] = play
        whose_turn = whose_turn_is_it(whose_turn)
        os.system('clear')
        board.print_board()
        time.sleep(0.5)

#Init Empty Boardlist:
my_b_list = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '], 
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],]

#Init Variables:
my_board = Board(my_b_list)
player_one = 'R'
player_two = 'Y'
whose_turn = 0

play_with_people(my_board, player_one, player_two, whose_turn)


