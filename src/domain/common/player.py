from domain.game import Game
from domain.common import Color


class Player:
    def __init__(self, game: Game, color: Color):
        self._game = game
        self._game.on_turn(self.turn)
        self._color = color

    def turn(self):
        raise NotImplementedError

    def pick(self):
        pass

    def on_pick(self, callback):
        pass

    def on_unpick(self, callback):
        pass

    def on_move(self, callback):
        pass
