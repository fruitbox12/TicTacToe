import Src.player


class HumanPlayer(Src.player.Player):
    def __init__(self, number, name):
        Src.player.Player.__init__(self, number, name)
