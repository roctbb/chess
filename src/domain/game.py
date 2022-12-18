from domain.board import Board, ImmutableBoard
from domain.common import GameRules, Color, Point
from typing import Type, List


class Game:
    def __init__(self, rules: Type[GameRules], side: Color):
        self._board = Board(rules.get_size(), side)
        self._rules = rules
        self._side = side
        self._turn = rules.get_first_turn()
        self.__turn_callbacks = []

        self._eaten = {
            Color.WHITE: [],
            Color.BLACK: []
        }

        self._rules.place_figures(self._board, self._side)

    def pick(self, point: Point) -> bool:
        if self._rules.can_pick(point, self._turn, self._board):
            return True
        return False

    def move(self, points: List[Point]) -> bool:
        if self._rules.can_move(points, self._turn, self._board):
            eaten = self._rules.attacked(points, self._turn, self._board)

            for point in eaten:
                self._eaten[Color.opposite(self._turn)].append(self._board.get(point))
                self._board.set(point, None)

            print(self._eaten)

            self._board.move(points[0], points[-1])
            self._rules.moved(points, self._turn, self._board)

            self._turn = Color.opposite(self._turn)
            for callback in self.__turn_callbacks:
                callback()

            return True
        return False

    def is_over(self) -> bool:
        return self._rules.is_over(self._turn, self._board)

    def on_turn(self, callback):
        self.__turn_callbacks.append(callback)

    def get_eaten_by(self, color: Color) -> tuple:
        return tuple(self._eaten[color])

    @property
    def board(self):
        return ImmutableBoard(self._board)

    @property
    def turn(self):
        return self._turn

    @property
    def side(self):
        return self._side
