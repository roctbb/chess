from domain.board import Board
from domain.common import GameRules, Point, Color
from domain.chess.figures import *
from domain.chess.rules.figure_rules import *

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


class StandardChessRules(GameRules):
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

    @classmethod
    def can_move(cls, start: Point, end: Point, turn: Color, board: Board) -> bool:
        if not cls.can_pick(start, turn, board):
            return False

        rule = cls._rules.get(board.get(start).LITERAL)
        if not rule:
            raise Exception("Rule for figure not found")

        if rule.can_move(start, end, turn, board):
            return True

        return False

    @classmethod
    def place_figures(cls, board: Board, color: Color) -> None:
        if color not in cls.DEFAULT_PLACEMENT:
            raise Exception("No placement for color")
        board.load_state(cls.DEFAULT_PLACEMENT[color])

    @classmethod
    def get_first_turn(cls):
        return Color.WHITE

    @classmethod
    def get_size(cls):
        return (8, 8)

    @classmethod
    def is_over(turn: Color, board: Board):
        raise NotImplementedError
