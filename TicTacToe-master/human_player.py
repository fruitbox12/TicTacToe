import player


class HumanPlayer(player.Player):
    def __init__(self, type, number, name, board):
        player.Player.__init__(self, type, number, name, board)

    # Override abstract method
    def play(self, row, col):
        player.Player.move(row, col)
