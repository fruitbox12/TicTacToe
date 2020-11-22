import Src.view
import Src.board
import Src.player
import Src.human_player
import random
import numpy


class Controller:
    def __init__(self):
        self.__rows = 3
        self.__cols = 3
        self.__min_players = 2
        self.__number_of_players = 2
        self.__board = Src.board.Board(self.__rows, self.__cols)
        self.__max_players = 2
        self.__current_player = 0
        self.__winning_player = 0
        self.__game_type = 0
        # Create the View Instance
        self.__view = Src.view.View(self, self.__rows, self.__cols, self.__min_players, self.__max_players)
        # FOR TEST PURPOSES ONLY

        self.play()

    def game_is_in_progress(self):
        in_progress = True
        current_row, current_col = self.__players[self.__current_player - 1].get_move()
        current_player = self.__players[self.__current_player - 1].get_number()
        # Check if the current Player won this game
        if self.__board.horizontal_winner(current_player, current_row) or\
                self.__board.vertical_winner(current_player, current_col) or \
                self.__board.diagonal_winner(current_player, current_row):
            self.__winning_player = current_player
            in_progress = False

        elif self.__board.game_is_a_draw():

            in_progress = False

        return in_progress

    def next_player(self):
        if self.__current_player < self.__max_players:
            self.__current_player += 1
        else:
            self.__current_player = 1

    def play(self):
        while not self.__game_type == 3:
            self.__game_type = self.__view.menu()

            if self.__game_type == 1:
                self.new_game(self.__game_type)
            elif self.__game_type == 2:
                self.__view.message("Player vs AI Player hasnt been added retard")
            else:
                self.__view.message("Thank you for playing TicTacToe")

    def new_game(self, game_type):
        self.__board = Src.board.Board(self.__rows, self.__cols)

        player_names = self.__view.get_player_names()
        self.__players = numpy.empty(self.__number_of_players, dtype=Src.player.Player)
        if game_type == 1:
            for number in range(1, self.__max_players + 1):
                self.__players[number - 1] = Src.human_player.HumanPlayer(number, player_names[number - 1])
            self.__view.message('Starting a Player vs Player Game')
        # starting player randomly
        if self.__winning_player > 0:
            self.__current_player = self.__winning_player
        else:
            self.__current_player = random.randint(1, self.__number_of_players)

        # the game loop
        while self.game_is_in_progress():
            # Display the board
            self.display_board()
            self.__view.message(str(self.__players[self.__current_player - 1].get_name()) + ', is your turn to play')

            available = False
            while not available:
                """"get the current players move (row, col)"""
                # Input and validate the current Player's move (row, col)
                row, col = self.__view.get_move()

                self.__view.message('Your move: row ' + str(row) + ', col ' + str(col))

                # Check the current player's move is available
                if self.__board.move(row, col, self.__current_player):
                    self.__players[self.__current_player - 1].move(row, col)
                    available = True

                    if self.game_is_in_progress():
                        self.next_player()
                else:
                    self.__view.message('That Board position is not available, please select another position')

        #Display the final board
        self.display_board()
        if self.__winning_player > 0:
            self.__view.message(self.__players[self.__current_player - 1].get_name() + " has won. Nice job retard!\n")
        else:
            self.__view.message("Nice job! No one won, DRAW!\n")


    def display_board(self):
        self.__view.message()
        horizontal = '\u2500'
        cross = '\u253c'
        vertical = '\u2502'
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                position = self.get_board_position(row, col)
                value = '   '
                if position == 1:
                    value = ' X '
                elif position == 2:
                    value = ' O '
                if col == 1 or col == 2:
                    value = value + vertical
                self.__view.message(value, end="")
            self.__view.message()
            if row == 1 or row == 2:
                self.__view.message(horizontal + horizontal + horizontal + cross + horizontal + horizontal + horizontal + cross + horizontal + horizontal + horizontal)
                # print('---------')
        self.__view.message()

    def get_board_position(self, row, col):
        return self.__board.get_board_position(row, col)

    def horizontal_winner(self):
        winner = False

        # Get the current player's move
        current_row, current_col = self.__players[self.__current_player - 1].get_move()
        number = self.__players[self.__current_player - 1].get_number()

        number_of_positions = 0

        for row in range(current_row, current_row + 1):
            for col in range(1, self.__cols + 1):
                position = self.get_board_position(row, col)

                if position == number:
                    number_of_positions += 1

        if number_of_positions == self.__cols:
            winner = True
        return winner

    def vertical_winner(self):
        winner = False

        # Get the current player's move
        current_row, current_col = self.__players[self.__current_player - 1].get_move()
        number = self.__players[self.__current_player - 1].get_number()

        number_of_positions = 0

        for col in range(current_col, current_col + 1):
            for row in range(1, self.__rows + 1):
                position = self.get_board_position(row, col)

                if position == number:
                    number_of_positions += 1

        if number_of_positions == self.__rows:
            winner = True
        return winner

    def diagonal_winner(self):
        winner = False

        # Get the current player's move
        current_row, current_col = self.__players[self.__current_player - 1].get_move()
        number = self.__players[self.__current_player - 1].get_number()

        number_of_positions = 0

        # Check for the left diagonal top left to bottom right
        for row in range(1, current_row + 1):
            for col in range(row, row + 1):
                position = self.get_board_position(row, col)

                if position == number:
                    number_of_positions += 1

        if number_of_positions == self.__cols:
            winner = True
            self.__view.message("left")
        else:
            number_of_positions = 0
            # Check for the right diagonal top right to bottom left
            for row in range(1, current_row + 1):
                for col in range(self.__cols - row + 1, self.__cols - row + 2):
                    position = self.get_board_position(row, col)

                    if position == number:
                        number_of_positions += 1

            if number_of_positions == self.__cols:
                winner = True
                self.__view.message("right")
        return winner

















