from typing import List

from domain.board import Board
from domain.chess.figures import *
from domain.chess.rules.figure_rules import *
from domain.common import Point, Color
from domain.rules import GameRules

DEFAULT_WHITE = """
rnbqkbnr
pppppppp
________
________
________
________
PPPPPPPP
RNBQKBNR
"""

DEFAULT_BLACK = """
RNBKQBNR
PPPPPPPP
________
________
________
________
pppppppp
rnbkqbnr
"""


class ChessRules(GameRules):
    DEFAULT_PLACEMENT = {
        Color.WHITE: DEFAULT_WHITE,
        Color.BLACK: DEFAULT_BLACK
    }

    _rules = {
        Bishop.LITERAL: BishopRule,
        Pawn.LITERAL: PawnRule,
        Knight.LITERAL: KnightRule,
        Rook.LITERAL: RookRule,
        King.LITERAL: KingRule,
        Queen.LITERAL: QueenRule
    }

    @staticmethod
    def can_pick(point: Point, turn: Color, board: Board) -> bool:
        figure = board.get(point)
        if not figure:
            return False

        if figure.color != turn:
            return False

        return True

    @staticmethod
    def attacked(points: List[Point], turn: Color, board: Board) -> List[Point]:
        answer = []

        if board.get(points[-1]):
            answer.append(points[-1])

        return answer

    @staticmethod
    def moved(points: List[Point], turn: Color, board: Board) -> None:
        pass

    @classmethod
    def can_move(cls, points: List[Point], turn: Color, board: Board) -> bool:
        if len(points) != 2:
            return False

        start = points[0]
        end = points[1]
        if not cls.can_pick(start, turn, board):
            return False

        rule = cls._rules.get(board.get(start).LITERAL)
        if not rule:
            raise Exception("Rule for figure not found")

        if rule.can_move([start, end], turn, board):
            return True

        return False

    @classmethod
    def place_figures(cls, board: Board, color: Color) -> None:
        if color not in cls.DEFAULT_PLACEMENT:
            raise Exception("No placement for color")
        board.load_state(cls.DEFAULT_PLACEMENT[color])

    @classmethod
    def check(cls, board: Board, color: Color):
        raise NotImplementedError

    @classmethod
    def mate(cls, board: Board, color: Color):
        raise NotImplementedError

    @classmethod
    def get_first_turn(cls):
        return Color.WHITE

    @classmethod
    def get_size(cls):
        return (8, 8)

    @classmethod
    def is_over(cls, color: Color, board: Board):
        raise NotImplementedError
