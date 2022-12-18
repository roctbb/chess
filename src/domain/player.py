from domain.common import Color, Point
from domain.game import Game


class Player:
    def __init__(self, game: Game, color: Color):
        self._game = game
        self._game.on_turn(self.make_turn)
        self._color = color

    def make_turn(self):
        raise NotImplementedError

    def pick(self, point: Point):
        pass

    def on_pick(self, callback):
        pass

    def on_unpick(self, callback):
        pass

    def on_move(self, callback):
        pass
