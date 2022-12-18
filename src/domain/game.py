from domain.board import Board, ImmutableBoard
from domain.common import GameRules, Color, Point
from typing import Type


class Game:
    def __init__(self, rules: Type[GameRules], side: Color):
        self._board = Board(rules.get_size(), side)
        self._rules = rules
        self._side = side
        self._turn = rules.get_first_turn()
        self.__turn_callbacks = []

        self._rules.place_figures(self._board, self._side)

    def pick(self, point: Point) -> bool:
        if self._rules.can_pick(point, self._turn, self._board):
            return True
        return False

    def move(self, start: Point, end: Point) -> bool:
        if self._rules.can_move(start, end, self._turn, self._board):
            self._board.move(start, end)
            self._turn = Color.opposite(self._turn)

            for callback in self.__turn_callbacks:
                callback()

            return True
        return False

    def is_over(self) -> bool:
        return self._rules.is_over(self._turn, self._board)

    def on_turn(self, callback):
        self.__turn_callbacks.append(callback)

    @property
    def board(self):
        return ImmutableBoard(self._board)

    @property
    def turn(self):
        return self._turn

    @property
    def side(self):
        return self._side
