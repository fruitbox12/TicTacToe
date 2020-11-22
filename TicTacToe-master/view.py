class View:
    def __init__(self, controller, rows, cols, min_players, max_players):
        self.__controller = controller
        self.__rows = rows
        self.__cols = cols
        self.__min_players = min_players
        self.__max_players = max_players
    def menu(self):
        menu_option = 0
        valid = False

        while not valid:
            print('Menu')
            print('1. Player vs. Player Game')
            print('2. New Player vs. AI Game')
            print('3. Exit')

            menu_option = int(input('Please select an option: '))

            if menu_option not in range(1, 4):
                print('Please select a valid option')
            elif menu_option == 2:
                print('Soorey the ai broke')
            else:
                valid = True

        return menu_option

    def get_player_names(self):
        player_name_list = []
        player = 0
        samename = False
        for self.__min_players in range(self.__max_players):
                player += 1
                name = str(input("Please enter your name Player " + str(player) + ". Press Enter to confirm "))
                player_name_list.append(name)
                print("Your name is: " + name)

        return player_name_list

    def message(self, message="", end="\n"):
        if len(end) == 0:
            print(message, end="")
        else:
            print(message)

    def get_move(self):
        """"""
        valid_row = False
        valid_col = False
        while not valid_row:
            try:
                rows = int(input('Please select a row between 1 and ' + str(self.__rows) + ': '))
            except ValueError:
                rows = 0
            if rows not in range(1, self.__rows + 1):
                print('Please select a valid option')
            else:
                valid_row = True
        while not valid_col:
            try:
                cols = int(input('Please select a col between ' + '1' + ' and ' + str(self.__cols) + ': '))
            except ValueError:
                cols = 0
            if cols not in range(1, self.__cols + 1):
                print('Please select a valid option')
            else:
                valid_col = True
        return rows, cols

    def get_move_one_loop(self):
        """"""
        valid_row = False
        valid_col = False
        valid = False
        while not valid:
            if not valid_row:
                try:
                    rows = int(input('Please select a row between 1 and ' + str(self.__rows) + ': '))
                except ValueError:
                    rows = 0
                if rows not in range(1, self.__rows+1):
                    print('Please select a valid option')
                    continue
                else:
                    valid_row = True
            try:
                cols = int(input('Please select a col between ' + '1' + ' and ' + str(self.cols) + ': '))
            except ValueError:
                cols = 0
            if cols not in range(1, self.__cols+1):
                print('Please select a valid option')
            else:
                valid_col = True
            if valid_row and valid_col:
                valid = True
        return rows, cols
"""
    def display_board(self):
        print()
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                position = self.__controller.getBoardPosition(row, col)
                value = '   '
                if position == 1:
                    value = ' X '
                elif position == 2:
                    value = ' O '
                if col == 1 or col == 2:
                    value = value + '|'
                print(value, end="")
            print()
            if row == 1 or row == 2:
                print('---------')
        print()
        #print('\u254b')

    def display_board_u(self):
        print()
        horizontal = '\u2500'
        cross = '\u253c'
        vertical = '\u2502'
        for row in range(1, self.__rows + 1):
            for col in range(1, self.__cols + 1):
                position = self.__controller.getBoardPosition(row, col)
                value = '   '
                if position == 1:
                    value = ' X '
                elif position == 2:
                    value = ' O '
                if col == 1 or col == 2:
                    value = value + vertical
                print(value, end="")
            print()
            if row == 1 or row == 2:
                print(horizontal + horizontal + horizontal + cross + horizontal + horizontal + horizontal + cross + horizontal + horizontal + horizontal)
                #print('---------')
        print()
"""
