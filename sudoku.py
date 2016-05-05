# #This is my sudoku program!

# def printboard(board):
#     for row in board:
    	

def getposition():
    posX = int(input('Enter a row value from 1 to 9: '))
    posY = int(input('Enter a column value from 1 to 9: '))
    return [(posX-1), (posY-1)]

def get_play():
	play = input("What number would goes here?")
	#play = int(play)
	return play

def updateboard(pos, play, board):
    board[pos[0]][pos[1]] = play
    

# def updateboard(pos, play):
#     board[pos[0]][pos[1]] = play
#     printboard()
        
# board = []

# for row in range(9): #Leave this alone
# 	board.append([])
# 	for column in range(9):
# 		board[row].append('x')


# # board = []
# # for i in range(9):
# # 	board.append([])
# # 	for j in range(9):
# # 		board[i].append('_')

# printboard(board)

def build_board():
	board = []
	for i in range(9):
		block = [[" ", " ", " "],
				 [" ", " ", " "],
				 [" ", " ", " "]]
		board.append(block)
	return board

 

def display(board):
    num=[]
    for i in board: #block level
        for subI in i: #row
            for subsubI in subI: #item
                num.append(subsubI)
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[0],num[1],num[2],num[9],num[10],num[11],num[18],num[19],num[20]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[3],num[4],num[5],num[12],num[13],num[14],num[21],num[22],num[23]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[6],num[7],num[8],num[15],num[16],num[17],num[24],num[25],num[26]))
    print("---------------------------------------")
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[27],num[28],num[29],num[36],num[37],num[38],num[45],num[46],num[47]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[30],num[31],num[32],num[39],num[40],num[41],num[48],num[49],num[50]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[33],num[34],num[35],num[42],num[43],num[44],num[51],num[52],num[53]))
    print("---------------------------------------")
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[54],num[55],num[56],num[63],num[64],num[65],num[72],num[73],num[74]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[57],num[58],num[59],num[66],num[67],num[68],num[75],num[76],num[77]))
    print("---------------------------------------")
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[60],num[61],num[62],num[69],num[70],num[71],num[78],num[79],num[80]))
    print("---------------------------------------")  
    return num


board = build_board()

position = getposition()
play = get_play()
updateboard(position, play, board)
display = display(board)

