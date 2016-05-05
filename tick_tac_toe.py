import random
import os

board = []

for i in range(3):
	board.append([])
	for j in range(3):
		board[i].append(['.'])

for i in range(3):
	for j in range(3):
		print(board[i][j])
	print