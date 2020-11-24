import view
import board
import player
import human_player
import ai_player
import random
import numpy


class Controller:
    def __init__(self):
        self.__rows = 3
        self.__cols = 3
        self.__min_players = 1
        self.__human_player = 1
        self.__ai_player = 2
        self.__number_of_players = 2
        self.__board = board.Board(self.__rows, self.__cols)
        self.__max_players = 2
        self.__current_player = 0
        self.__winning_player = 0
        self.__game_type = 0
        # Create the View Instance
        self.__view = view.View(self, self.__rows, self.__cols, self.__min_players, self.__max_players)
        # FOR TEST PURPOSES ONLY

        self.play()

    def game_is_in_progress(self):
        in_progress = True
        current_row, current_col = self.__players[self.__current_player - 1].get_move()
        current_player = self.player = self.__players[self.__current_player - 1]
        # Check if the current Player won this game
        if current_player.horizontal_winner(current_row) or\
               current_player.vertical_winner(current_col) or \
               current_player.diagonal_winner(current_row):
                self.__winning_player = self.__current_player
                in_progress = False
            
        if self.game_is_a_draw(): 
            in_progress = False

        return in_progress

    def game_is_a_draw(self):
        empty_positions = 0
        #Check if all squares are filled
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                position = self.__board.get_board_position(row, col)

                if position == self.__board.get_empty():
                    empty_positions += 1

        return empty_positions <= 1

    def next_player(self):
        if self.__current_player < self.__max_players:
            self.__current_player += 1
        else:
            self.__current_player = 1

    def play(self):
        while not self.__game_type == 4:
            self.__game_type = self.__view.menu()
            """Game types: 1 PVP 2 PVAI 3 AI v AI 4 Exit """
            if self.__game_type == 1 or self.__game_type == 2 or self.__game_type == 3:
                self.new_game(self.__game_type)
            elif self.__game_type == 4:
                self.__view.message("Thank you for playing tic tac toe")
            else:
                raise Exception("controller.play(): Invalid game type: " + self.__game_type)



    def new_game(self, game_type):
        self.__board = board.Board(self.__rows, self.__cols)

        player_names = self.__view.get_player_names(self.__game_type)
        self.__players = numpy.empty(self.__number_of_players, dtype=player.Player)
        if game_type == 1:
            for number in range(1, self.__max_players + 1):
                self.__players[number - 1] = human_player.HumanPlayer(self.__human_player, number, player_names[number - 1], self.__board)
            self.__view.message('Starting a Player vs Player Game')

        elif game_type == 2:
            player_number = 1;
           
            self.__players[0] = human_player.HumanPlayer(self.__human_player,player_number, player_names[0], self.__board)

            for number in range(player_number + 1, self.__max_players + 1):
                self.__players[number - 1] = ai_player.AIPlayer(self.__ai_player,number, "AI-" + str(number), self.__board)

            self.__view.message('Starting a Player vs AI Player Game')

        elif game_type == 3:
            for number in range(1, self.__max_players + 1):
                self.__players[number - 1] = ai_player.AIPlayer(self.__ai_player,number, "AI-" + str(number), self.__board)

            self.__view.message('Starting a AI Player vs AI Player Game')
        # starting player randomly
        if self.__winning_player > 0:
            self.__current_player = self.__winning_player
        else:
            self.__current_player = random.randint(1, self.__number_of_players)

        # the game loop
        # IS THE CONDITION CORRECT? INSIDE THE LOOP WE'RE CALLING game_is_in_progress()...
        game_in_progress = True
        while game_in_progress:
            
            self.__view.message(str(self.__players[self.__current_player - 1].get_name()) + ', is your turn to play')


            # THIS CONDITION DOES NOT APPLY TO AN AI...
            """"get the current players move (row, col)"""
            # Input and validate the current Player's move (row, col)
            if self.__players[self.__current_player -1].get_type() == self.__human_player:
                # Display the board
                self.display_board()

                available = False

                while not available:
                    row, col = self.__view.get_move()

                    self.__view.message('Your move: row ' + str(row) + ', col ' + str(col))

                    # Check the current player's move is available
                    if self.__board.move(row, col, self.__current_player):
                        self.display_board()
                        available = True
                    else:
                        self.__view.message('That Board position is not available, please select another position')          
            else:
                # Tell the AI to play
                self.__players[self.__current_player -1].play()
                row, col =  self.__players[self.__current_player -1].get_position()
                self.display_board()

                if self.__board.move(row, col, self.__current_player):
                    self.display_board()
                else:
                    raise Exception("controller.new_game(): Invalid AI player move. Board position not available.")
                # Display the board

                self.__view.message('Your move: row ' + str(row) + ', col ' + str(col))
            if self.game_is_in_progress():
                self.next_player()
            else:
                game_in_progress = False

        #Display the final board
        self.display_board()
        if self.__winning_player > 0:
            self.__view.message(self.__players[self.__current_player - 1].get_name() + " has won. Nice job buddy!\n")
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

















