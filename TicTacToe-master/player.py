

class Player:
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        self.__row = 0
        self.__col = 0

    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def move(self, row, col):
        self.__row = row
        self.__col = col

    def get_move(self):
        return self.__row, self.__col


