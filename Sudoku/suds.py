#Testing my sudoku board:
import os
board = []
my_looper = True
board_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_4 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_5 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_6 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_7 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
board_set_9 = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def position_checker(pos):
	if board[pos[0]][pos[1]][pos[2]] != 0:
		print("Something is there already!")
		print("Please try again.")
		pos = getposition()
		os.system('clear')
		position_checker(pos)
	return pos

def board_set_checker(board, board_set_1):
	for i in board[0]:
		if i in board_set_1: board_set.remove(i)

		

def play_checker(pos, play):
	check_list = []
	check_list.append(board[pos[0]][0][0])
	check_list.append(board[pos[0]][0][1])
	check_list.append(board[pos[0]][0][2])
	check_list.append(board[pos[0]][1][0])
	check_list.append(board[pos[0]][1][1])
	check_list.append(board[pos[0]][1][2])
	check_list.append(board[pos[0]][2][0])
	check_list.append(board[pos[0]][2][1])
	check_list.append(board[pos[0]][2][2])

	if play in check_list:
		print("That number doesn't go there!")
		print("Try again!")
		play = get_play()
		play_checker(pos, play)
	return play


def ugly_score_machine(board):
 	if (((board[0][0][0] + board[0][0][1] + board[0][0][2] + board[0][1][0] + board[0][1][1] + board[0][1][2] + board[0][2][0] + board[0][2][1] + board[0][2][2]) == 45) and
 	((board[1][0][0] + board[1][0][1] + board[1][0][2] + board[1][1][0] + board[1][1][1] + board[1][1][2] + board[1][2][0] + board[1][2][1] + board[1][2][2]) == 45) and
 	((board[2][0][0] + board[2][0][1] + board[2][0][2] + board[2][1][0] + board[2][1][1] + board[2][1][2] + board[2][2][0] + board[2][2][1] + board[2][2][2]) == 45) and
 	((board[3][0][0] + board[3][0][1] + board[3][0][2] + board[3][1][0] + board[3][1][1] + board[3][1][2] + board[3][2][0] + board[3][2][1] + board[3][2][2]) == 45) and
 	((board[4][0][0] + board[4][0][1] + board[4][0][2] + board[4][1][0] + board[4][1][1] + board[4][1][2] + board[4][2][0] + board[4][2][1] + board[4][2][2]) == 45) and
 	((board[5][0][0] + board[5][0][1] + board[5][0][2] + board[5][1][0] + board[5][1][1] + board[5][1][2] + board[5][2][0] + board[5][2][1] + board[5][2][2]) == 45) and
 	((board[6][0][0] + board[6][0][1] + board[6][0][2] + board[6][1][0] + board[6][1][1] + board[6][1][2] + board[6][2][0] + board[6][2][1] + board[6][2][2]) == 45) and
 	((board[7][0][0] + board[7][0][1] + board[7][0][2] + board[7][1][0] + board[7][1][1] + board[7][1][2] + board[7][2][0] + board[7][2][1] + board[7][2][2]) == 45) and
 	((board[8][0][0] + board[8][0][1] + board[8][0][2] + board[8][1][0] + board[8][1][1] + board[8][1][2] + board[8][2][0] + board[8][2][1] + board[8][2][2]) == 45) and
 	((board[0][0][0] + board[0][1][0] + board[0][2][0] + board[3][0][0] + board[3][1][0] + board[3][2][0] + board[6][0][0] + board[6][1][0] + board[6][2][0]) == 45) and
 	((board[0][0][1] + board[0][1][1] + board[0][2][1] + board[3][0][1] + board[3][1][1] + board[3][2][1] + board[6][0][1] + board[6][1][1] + board[6][2][1]) == 45) and
 	((board[0][0][2] + board[0][1][2] + board[0][2][2] + board[3][0][2] + board[3][1][2] + board[3][2][2] + board[6][0][2] + board[6][1][2] + board[6][2][2]) == 45) and
 	((board[1][0][0] + board[1][1][0] + board[1][2][0] + board[4][0][0] + board[4][1][0] + board[4][2][0] + board[7][0][0] + board[7][1][0] + board[7][2][0]) == 45) and
 	((board[1][0][1] + board[1][1][1] + board[1][2][1] + board[4][0][1] + board[4][1][1] + board[4][2][1] + board[7][0][1] + board[7][1][1] + board[7][2][1]) == 45) and
 	((board[1][0][2] + board[1][1][2] + board[1][2][2] + board[4][0][2] + board[4][1][2] + board[4][2][2] + board[7][0][2] + board[7][1][2] + board[7][2][2]) == 45) and
 	((board[2][0][0] + board[2][1][0] + board[2][2][0] + board[5][0][0] + board[5][1][0] + board[5][2][0] + board[8][0][0] + board[8][1][0] + board[8][2][0]) == 45) and
 	((board[2][0][1] + board[2][1][1] + board[2][2][1] + board[5][0][1] + board[5][1][1] + board[5][2][1] + board[8][0][1] + board[8][1][1] + board[8][2][1]) == 45) and
 	((board[2][0][2] + board[2][1][2] + board[2][2][2] + board[5][0][2] + board[5][1][2] + board[5][2][2] + board[8][0][2] + board[8][1][2] + board[8][2][2]) == 45)):
 		print("You win!")
 		print_board(board)
 		return True
 	else: return False

def easy_board_two(board):
	board[0][1][1] = 9
	board[0][1][2] = 8
	board[1][1][0] = 7
	board[1][1][1] = 2
	board[1][2][2] = 4
	board[2][0][1] = 9
	board[2][0][2] = 7
	board[2][1][0] = 1
	board[2][1][2] = 6
	board[2][2][0] = 8
	board[2][2][1] = 5
	board[2][2][2] = 3
	board[3][0][1] = 3
	board[3][2][0] = 1
	board[3][2][1] = 4
	board[4][0][2] = 9
	board[4][1][0] = 8
	board[4][1][1] = 1
	board[4][1][2] = 2
	board[4][2][0] = 5
	board[5][0][1] = 7
	board[5][0][2] = 1
	board[5][2][1] = 2
	board[6][0][0] = 5
	board[6][0][1] = 8
	board[6][0][2] = 3
	board[6][1][0] = 2
	board[6][1][2] = 6
	board[6][2][0] = 9
	board[6][2][1] = 1
	board[7][0][0] = 4
	board[7][1][1] = 5
	board[7][1][2] = 3
	board[8][1][0] = 9
	board[8][1][1] = 8
	return board


def easy_board_one(board):
	board[0][0][0] = 2
	board[0][0][2] = 8
	board[0][1][1] = 3
	board[0][2][0] = 1
	board[0][2][2] = 6
	board[1][0][2] = 9
	board[1][2][0] = 4
	board[2][0][0] = 7
	board[2][0][1] = 6
	board[2][1][0] = 8
	board[2][1][2] = 5
	board[2][2][0] = 9
	board[3][0][1] = 2
	board[3][1][0] = 6
	board[3][1][1] = 4
	board[3][1][2] = 3
	board[3][2][0] = 8
	board[4][0][2] = 5
	board[4][2][0] = 2
	board[5][0][2] = 8
	board[5][1][0] = 2
	board[5][1][1] = 5
	board[5][1][2] = 7
	board[5][2][1] = 3
	board[6][0][2] = 4
	board[6][1][0] = 3
	board[6][1][2] = 2
	board[6][2][1] = 8
	board[6][2][2] = 1
	board[7][0][2] = 7
	board[7][2][0] = 5
	board[8][0][0] = 3
	board[8][0][2] = 2
	board[8][1][1] = 7
	board[8][2][0] = 4
	board[8][2][2] = 6
	return board

	

def user_continue(looper):
	user_choice = input("Continue?: \n")
	if user_choice == 'n':looper = False
	return looper

def updateboard(pos, play, board):
	board[pos[0]][pos[1]][pos[2]] = play
	return board

def get_play():
	play = input("What number should we put here?")
	play = int(play)
	return play

def getposition():
	posZ = input("Enter a block value from 1 to 9: ")
	if posZ == 'n': quit()
	else:
		posZ = int(posZ)
		posX = int(input('Enter a row value from 1 to 3: '))
		posY = int(input('Enter a column value from 1 to 3: '))
	return [(posZ-1), (posX-1), (posY-1)]

def build_board():
	"""This function builds our board. Unfortunately, it looks bad.
	We will have to print it in a different function."""
	board = []
	for i in range(9):
		block = [[0, 0, 0],
				 [0, 0, 0],
				 [0, 0, 0]]
		board.append(block)
	return board

def print_board(board):
	"""This function will print the board."""
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[0][0][0],board[0][0][1],board[0][0][2],board[1][0][0],board[1][0][1],board[1][0][2],board[2][0][0],board[2][0][1],board[2][0][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[0][1][0],board[0][1][1],board[0][1][2],board[1][1][0],board[1][1][1],board[1][1][2],board[2][1][0],board[2][1][1],board[2][1][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[0][2][0],board[0][2][1],board[0][2][2],board[1][2][0],board[1][2][1],board[1][2][2],board[2][2][0],board[2][2][1],board[2][2][2]))
	print("---------------------------------------")
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[3][0][0],board[3][0][1],board[3][0][2],board[4][0][0],board[4][0][1],board[4][0][2],board[5][0][0],board[5][0][1],board[5][0][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[3][1][0],board[3][1][1],board[3][1][2],board[4][1][0],board[4][1][1],board[4][1][2],board[5][1][0],board[5][1][1],board[5][1][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[3][2][0],board[3][2][1],board[3][2][2],board[4][2][0],board[4][2][1],board[4][2][2],board[5][2][0],board[5][2][1],board[5][2][2]))
	print("---------------------------------------")
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[6][0][0],board[6][0][1],board[6][0][2],board[7][0][0],board[7][0][1],board[7][0][2],board[8][0][0],board[8][0][1],board[8][0][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[6][1][0],board[6][1][1],board[6][1][2],board[7][1][0],board[7][1][1],board[7][1][2],board[8][1][0],board[8][1][1],board[8][1][2]))
	print("---------------------------------------")
	print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(board[6][2][0],board[6][2][1],board[6][2][2],board[7][2][0],board[7][2][1],board[7][2][2],board[8][2][0],board[8][2][1],board[8][2][2]))
	print("---------------------------------------")




board = build_board()

board = easy_board_two(board)
while not ugly_score_machine(board):
	print_board(board)
	pos = getposition()
	position_checker(pos)
	play = get_play()
	play_checker(pos, play)
	board = updateboard(pos, play, board)
	os.system('clear')
	#print_board(board)
