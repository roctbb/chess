from domain.common import FigureRule, Point, Color
from domain.board import Board


class KnightRule(FigureRule):
    @staticmethod
    def can_move(start: Point, end: Point, turn: Color, board: Board) -> bool:
        return False