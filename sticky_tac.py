class DictTTTBoard:
    def __init__(self):
        self.pos_to_token = {
            'a1': " ", 'b1': " ", 'c1': " ",
            'a2': " ", 'b2': 'X', 'c2': " ",
            'a3': " ", 'b3': " ", 'c3': " ",
        }

    def place(self, x, y, player):
        my_x = ['a', 'b', 'c']
        my_y = ['1', '2', '3']
        my_place = '{}{}'.format(my_x[x], my_y[y])
        self.pos_to_token[my_place] = player


    def won(self):
        #Horizontal
        if ((self.pos_to_token['a1'] == 
            self.pos_to_token['a2'] == self.pos_to_token['a3']) and
           (self.pos_to_token['a1'] != ' ')):
            return self.pos_to_token['a1']
        elif ((self.pos_to_token['b1'] ==
              self.pos_to_token['b2'] == self.pos_to_token['b3']) and
             (self.pos_to_token['b1'] != ' ')):
            return self.pos_to_token['b1']
        elif ((self.pos_to_token['c1'] ==
              self.pos_to_token['c2'] == self.pos_to_token['c3']) and
             (self.pos_to_token['c1'] != ' ')):
            return self.pos_to_token['c1']
        #Vertical
        elif ((self.pos_to_token['a1'] == 
            self.pos_to_token['b1'] == self.pos_to_token['c1']) and
           (self.pos_to_token['a1'] != ' ')):
            return self.pos_to_token['a1']
        elif ((self.pos_to_token['a2'] ==
              self.pos_to_token['b2'] == self.pos_to_token['c2']) and
             (self.pos_to_token['a2'] != ' ')):
            return self.pos_to_token['a2']
        elif ((self.pos_to_token['a3'] ==
              self.pos_to_token['b3'] == self.pos_to_token['c3']) and
             (self.pos_to_token['a3'] != ' ')):
            return self.pos_to_token['a3']
        #Diagonal
        elif ((self.pos_to_token['a1'] == 
            self.pos_to_token['b2'] == self.pos_to_token['c3']) and
           (self.pos_to_token['a1'] != ' ')):
            return self.pos_to_token['a1']
        elif ((self.pos_to_token['a3'] ==
              self.pos_to_token['b2'] == self.pos_to_token['c1']) and
             (self.pos_to_token['a3'] != ' ')):
            return self.pos_to_token['a3']


    def __str__(self):
        my_str= (' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '                '
                 .format(self.pos_to_token['a1'],
                 self.pos_to_token['a2'], self.pos_to_token['a3'],
                 self.pos_to_token['b1'], self.pos_to_token['b2'],
                 self.pos_to_token['b3'], self.pos_to_token['c1'],
                 self.pos_to_token['c2'], self.pos_to_token['c3']))
        return my_str
        


class ListListTTTBoard:
    def __init__(self):
        self.rows = [
            [" ", " ", " "],
            [" ", 'X', " "],
            [" ", " ", " "],
        ]

    def place(self, x, y, player):
        self.rows[x][y] = player

    def won(self):
        #Horizontal
        if ((self.rows[0][0] ==
            self.rows[0][1] == self.rows[0][2]) and
            self.rows[0][0] != ' '):
            return self.rows[0][0]
        elif ((self.rows[1][0] ==
              self.rows[1][1] == self.rows[1][2]) and
              self.rows[1][0] != ' '):
            return self.rows[1][0]
        elif ((self.rows[2][0] ==
              self.rows[2][1] == self.rows[2][2]) and
              self.rows[2][0] != ' '):
            return self.rows[2][0]
        #Vertical
        elif ((self.rows[0][0] ==
            self.rows[1][0] == self.rows[2][0]) and
            self.rows[0][0] != ' '):
            return self.rows[0][0]
        elif ((self.rows[0][1] ==
              self.rows[1][1] == self.rows[2][1]) and
              self.rows[0][1] != ' '):
            return self.rows[0][1]
        elif ((self.rows[0][2] ==
              self.rows[1][2] == self.rows[2][2]) and
              self.rows[0][1] != ' '):
            return self.rows[0][2]
        #Diagonal
        elif ((self.rows[0][0] ==
            self.rows[1][1] == self.rows[2][2]) and
            self.rows[0][0] != ' '):
            return self.rows[0][0]
        elif ((self.rows[0][2] ==
              self.rows[1][1] == self.rows[2][0]) and
              self.rows[0][2] != ' '):
            return self.rows[0][2]

    def __str__(self):
        my_str= (' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '                '
                 .format(self.rows[0][0],
                 self.rows[0][1], self.rows[0][2],
                 self.rows[1][0], self.rows[1][1],
                 self.rows[1][2], self.rows[2][0],
                 self.rows[2][1], self.rows[2][2]))
        return my_str


class CoordsTTTBoard:
    def __init__(self):
        self.x_y_token_triplets = [
            (1, 1, 'X'),
        ]

    def place(self, x, y, player):
        my_tup = (x, y, player)
        self.x_y_token_triplets.append(my_tup)

    def won(self):
        my_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i, j, k in self.x_y_token_triplets:
            my_list[i][j] = k
        #Horizontal
        if ((my_list[0][0] ==
            my_list[0][1] == my_list[0][2]) and
            my_list[0][0] != ' '):
            return my_list[0][0]
        elif ((my_list[1][0] ==
              my_list[1][1] == my_list[1][2]) and
              my_list[1][0] != ' '):
            return my_list[1][0]
        elif ((my_list[2][0] ==
              my_list[2][1] == my_list[2][2]) and
              my_list[2][0] != ' '):
            return my_list[2][0]
        #Vertical
        elif ((my_list[0][0] ==
            my_list[1][0] == my_list[2][0]) and
            my_list[0][0] != ' '):
            return my_list[0][0]
        elif ((my_list[0][1] ==
              my_list[1][1] == my_list[2][1]) and
              my_list[0][1] != ' '):
            return my_list[0][1]
        elif ((my_list[0][2] ==
              my_list[1][2] == my_list[2][2]) and
              my_list[0][1] != ' '):
            return my_list[0][2]
        #Diagonal
        elif ((my_list[0][0] ==
            my_list[1][1] == my_list[2][2]) and
            my_list[0][0] != ' '):
            return my_list[0][0]
        elif ((my_list[0][2] ==
              my_list[1][1] == my_list[2][0]) and
              my_list[0][2] != ' '):
            return my_list[0][2]


    def __str__(self):
        my_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for i, j, k in self.x_y_token_triplets:
            my_list[i][j] = k
        my_str= (' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '___________\n'
                 ' {} | {} | {} \n'
                 '                '
                 .format(my_list[0][0],
                 my_list[0][1], my_list[0][2],
                 my_list[1][0], my_list[1][1],
                 my_list[1][2], my_list[2][0],
                 my_list[2][1], my_list[2][2]))
        return my_str



def play(board):
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    print(board)
    board.place(0, 2, 'O')
    print(board)
    assert board.won() is None
    board.place(1, 2, 'X')
    print(board)
    assert board.won() == 'X'


def main():
    board1 = DictTTTBoard()
    play(board1)
    board2 = ListListTTTBoard()
    play(board2)
    board3 = CoordsTTTBoard()
    play(board3)


main()