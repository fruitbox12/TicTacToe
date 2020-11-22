import numpy


class Board:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__empty = 0
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

    def horizontal_winner(self, player_number, current_row):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        for row in range(current_row, current_row + 1):
            for col in range(1, self.__cols + 1):
                position = self.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1

        if number_of_positions == self.__cols:
            winner = True
        return winner

    def vertical_winner(self, player_number, current_col):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        for col in range(current_col, current_col + 1):
            for row in range(1, self.__rows + 1):
                position = self.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1

        if number_of_positions == self.__rows:
            winner = True
        return winner

    def diagonal_winner(self, player_number, current_row):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        # Check for the left diagonal top left to bottom right
        for row in range(1, current_row + 1):
            for col in range(row, row + 1):
                position = self.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1

        if number_of_positions == self.__cols:
            winner = True
        else:
            number_of_positions = 0
            # Check for the right diagonal top right to bottom left
            for row in range(1, current_row + 1):
                for col in range(self.__cols - row + 1, self.__cols - row + 2):
                    position = self.get_board_position(row, col)

                    if position == player_number:
                        number_of_positions += 1

            if number_of_positions == self.__cols:
                winner = True

        return winner

    def game_is_a_draw(self):
        empty_positions = 0
        #Check if all squares are filled
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                position = self.get_board_position(row, col)

                if position == self.__empty:
                    empty_positions += 1

        return empty_positions <= 1
