from typing import List

from domain.board import Board
from domain.common import FigureRule, Point, Color


class QueenRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        return False
