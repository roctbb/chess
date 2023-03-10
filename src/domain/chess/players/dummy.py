from domain.common import Color
from domain.player import Player


class DummyPlayer(Player):
    def make_turn(self):
        if self._game.turn == self._color:
            if self._game.side == Color.WHITE:
                if self._color == Color.WHITE:
                    self._game.move([(0, 6), (0, 4)])
                else:
                    self._game.move([(0, 1), (0, 3)])
            else:
                if self._color == Color.WHITE:
                    self._game.move([(0, 1), (0, 3)])
                else:
                    self._game.move([(0, 6), (0, 4)])
