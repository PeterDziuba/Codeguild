class ListListTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list
    of rows, each with three slots.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    [
        ['X', ' ', ' '],
        [' ', 'X', 'O'],
        [' ', ' ', ' '],
    ]
    """

    def __init__(self):
        """Initializes an empty board."""
        self.rows = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        self.rows[y][x] = player

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        # Horizontal
        for x in range(3):
            for y in range(1):
                if ((self.rows[x][y] ==
                     self.rows[x][y + 1] == self.rows[x][y + 2]) and
                        (self.rows[x][y] != " ")):
                    return self.rows[x][y]
        # Vertical
        for x in range(1):
            for y in range(3):
                if ((self.rows[x][y] ==
                     self.rows[x + 1][y] == self.rows[x + 2][y]) and
                        (self.rows[x][y] != " ")):
                    return self.rows[x][y]

        # Diagonal
        if ((self.rows[0][0] ==
             self.rows[1][1] == self.rows[2][2]) and
           self.rows[0][0] != ' '):
            return self.rows[0][0]

        elif ((self.rows[0][2] ==
              self.rows[1][1] == self.rows[2][0]) and
              self.rows[0][2] != ' '):
            return self.rows[0][2]

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """
        my_str = ('{}|{}|{}\n'
                  '{}|{}|{}\n'
                  '{}|{}|{}\n'
                  .format(self.rows[0][0],
                          self.rows[0][1], self.rows[0][2],
                          self.rows[1][0], self.rows[1][1],
                          self.rows[1][2], self.rows[2][0],
                          self.rows[2][1], self.rows[2][2]))
        return my_str


class DictTTTBoard:
    """Tic-Tac-Toe board that implements storage as a flat
    dictionary of slots.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    {
        'a1': 'X', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': 'X', 'c2': 'O',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }
    """

    def __init__(self):
        """Initializes an empty board."""
        self.pos_to_token = {
            'a1': ' ', 'b1': ' ', 'c1': ' ',
            'a2': ' ', 'b2': ' ', 'c2': ' ',
            'a3': ' ', 'b3': ' ', 'c3': ' ',
        }

    def place(self, x, y, token):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        my_x = ['a', 'b', 'c']
        my_y = ['1', '2', '3']
        my_place = '{}{}'.format(my_x[y], my_y[x])
        self.pos_to_token[my_place] = token

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        my_x = ['a', 'b', 'c']
        my_y = ['1', '2', '3']
        for i in my_x:
            for j in my_y:
                # Horizontal
                if ((self.pos_to_token[i + my_y[0]] ==
                    self.pos_to_token[i + my_y[1]] ==
                    self.pos_to_token[i + my_y[2]]) and
                   (self.pos_to_token[i + my_y[0]] != " ")):
                    return self.pos_to_token[i + my_y[0]]

                # Vertical
                elif ((self.pos_to_token[my_x[0] + j] ==
                      self.pos_to_token[my_x[1] + j] ==
                      self.pos_to_token[my_x[2] + j]) and
                      (self.pos_to_token[my_x[0] + j] != " ")):
                    return self.pos_to_token[my_x[0] + j]

        # Diagonal
        if ((self.pos_to_token['a1'] ==
           self.pos_to_token['b2'] == self.pos_to_token['c3']) and
           (self.pos_to_token['a1'] != ' ')):
            return self.pos_to_token['a1']

        elif ((self.pos_to_token['a3'] ==
              self.pos_to_token['b2'] == self.pos_to_token['c1']) and
              (self.pos_to_token['a3'] != ' ')):
            return self.pos_to_token['a3']

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """
        my_str = ('{}|{}|{}\n'
                  '{}|{}|{}\n'
                  '{}|{}|{}\n'
                  .format(self.pos_to_token['a1'],
                          self.pos_to_token['a2'], self.pos_to_token['a3'],
                          self.pos_to_token['b1'], self.pos_to_token['b2'],
                          self.pos_to_token['b3'], self.pos_to_token['c1'],
                          self.pos_to_token['c2'], self.pos_to_token['c3']))
        return my_str


class CoordsTTTBoard:
    """Tic-Tac-Toe board that implements storage as a list of x, y, token triplets.
    An empty board is an empty list.
    Each token that is on the board adds one item to the triplet list.
    The following board results in the following data structure.
    X| |
     |X|O
     | |
    [(0, 0, 'X'), (1, 1, 'X'), (2, 1, 'O')]
    """

    def __init__(self):
        """Initalizes an empty board."""
        self.x_y_token_triplets = []

    def place(self, x, y, player):
        """Places a token on the board at some given coordinates.
        0, 0 is the top-left.
        `player` is either 'X' or 'O'
        """
        my_tup = (y, x, player)
        self.x_y_token_triplets.append(my_tup)

    def won(self):
        """Return which token type won ('X' or 'O') or None if no one
        has won yet."""
        my_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i, j, k in self.x_y_token_triplets:
            my_list[i][j] = k

        # Horizontal
        for x in range(3):
            for y in range(1):
                if ((my_list[x][y] ==
                    my_list[x][y + 1] == my_list[x][y + 2]) and
                        (my_list[x][y] != " ")):
                    return my_list[x][y]

        # Vertical
        for x in range(1):
            for y in range(3):
                if ((my_list[x][y] ==
                    my_list[x + 1][y] == my_list[x + 2][y]) and
                        (my_list[x][y] != " ")):
                    return my_list[x][y]

        # Diagonal
        if ((my_list[0][0] ==
            my_list[1][1] == my_list[2][2]) and
                my_list[0][0] != ' '):
            return my_list[0][0]

        elif ((my_list[0][2] ==
              my_list[1][1] == my_list[2][0]) and
                my_list[0][2] != ' '):
            return my_list[0][2]

    def __str__(self):
        """Returns a string representation of the board.
        Should be three rows with each cell separated by a '|'.
        X| |
         |X|O
         | |
        """
        my_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for i, j, k in self.x_y_token_triplets:
            my_list[i][j] = k
        my_str = ('{}|{}|{}\n'
                  '{}|{}|{}\n'
                  '{}|{}|{}\n'
                  .format(my_list[0][0],
                          my_list[0][1], my_list[0][2],
                          my_list[1][0], my_list[1][1],
                          my_list[1][2], my_list[2][0],
                          my_list[2][1], my_list[2][2]))
        return my_str


def play(board):
    """Plays a test game on an empty board.
    Asserts that the board is working properly.
    """
    board.place(1, 1, 'X')
    print(board)
    board.place(0, 0, 'O')
    print(board)
    board.place(1, 0, 'X')
    assert str(board) == "O|X| \n |X| \n | | \n"
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


if __name__ == '__main__':
    main()
