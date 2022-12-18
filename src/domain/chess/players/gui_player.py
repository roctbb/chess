from domain.common import Color, Point
from domain.game import Game
from domain.player import Player


class GuiPlayer(Player):
    def __init__(self, game: Game, color: Color):
        super().__init__(game, color)
        self._turn_from = None
        self._pick_callback = None
        self._unpick_callback = None

    def make_turn(self):
        pass

    def pick(self, point: Point):
        if self._game.turn == self._color:
            if self._unpick_callback:
                self._unpick_callback()

            if not self._turn_from:
                if self._game.pick(point):
                    self._turn_from = point

                    if self._pick_callback:
                        self._pick_callback(point)
            else:
                self._game.move([self._turn_from, point])
                self._turn_from = None

    def on_pick(self, callback):
        self._pick_callback = callback

    def on_unpick(self, callback):
        self._unpick_callback = callback
