

class Player:
    def __init__(self, type, number, name, board):
        self.__type = type
        self.__number = number
        self.__name = name
        self.__row = 0
        self.__col = 0
        self.__board = board
        self.__rows = board.get_rows()
        self.__cols = board.get_cols()

    def get_number(self):
        return self.__number

    def get_position(self):
        return self.__row, self.__col  

    def get_name(self):
        return self.__name

    def move(self, row, col):
        self.__row = row
        self.__col = col

    def get_move(self):
        return self.__row, self.__col

    def get_board(self):
        return self.__board

    def get_type(self):
        return self.__type

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    # Abstract method
    def play(self, row, col):
        pass

    def horizontal_winner(self, current_row):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        player_number = self.get_number()
        board = self.get_board()
        cols = board.get_cols()

        for row in range(1, cols + 1):
            for col in range(1,  cols + 1):
                position = board.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1
            if number_of_positions == cols:
                winner = True

                break
            else:
                number_of_positions = 0
        return winner

    def vertical_winner(self, current_col):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        player_number = self.get_number()
        board = self.get_board()

        rows = board.get_rows()


        for col in range(1, rows + 1):
            for row in range(1, rows + 1):
                position = board.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1

            if number_of_positions == rows:
                winner = True

                break
            else:
                number_of_positions = 0

            
        return winner

    def diagonal_winner(self, current_row):
        winner = False

        # Get the current player's move

        number_of_positions = 0

        player_number = self.get_number()
        board = self.get_board()

        cols = board.get_cols()

        # Check for the left diagonal top left to bottom right
        for row in range(1, cols + 1):
            for col in range(row, row + 1):
                position = board.get_board_position(row, col)

                if position == player_number:
                    number_of_positions += 1

        if number_of_positions == cols:
            winner = True

        else:
            number_of_positions = 0
            # Check for the right diagonal top right to bottom left
            for row in range(1, cols + 1):
                for col in range(cols - row + 1, cols - row + 2):
                    position = board.get_board_position(row, col)

                    if position == player_number:
                        number_of_positions += 1

            if number_of_positions == cols:
                winner = True

        return winner

    


