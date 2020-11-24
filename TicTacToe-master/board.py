import numpy


class Board:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__empty = 0
        self.__invalid = -1
        self.__board = numpy.zeros((self.__rows, self.__cols), dtype=int)
        

        """FOR TEST PURPOSES ONLY
        print(self.board)
        self.board[1][1] = 1
        print(self.board)
        """
    def is_available(self, row, col):
        return self.__board[row - 1][col - 1] == 0

    def move(self, row, col, number):
        available = False

        if self.__board[row - 1][col - 1] == 0:
            self.__board[row - 1][col - 1] = number
            available = True

        return available

    def get_board_position(self, row, col):
        return self.__board[row - 1][col - 1]

    def get_rows(self):
        return self.__rows
    
    def get_cols(self):
        return self.__cols

    def get_empty(self):
        return self.__empty

    def get_invalid(self):
        return self.__invalid
    

