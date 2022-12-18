from domain.common import FigureRule, Point, Color
from domain.board import Board
from typing import List


class BishopRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        return False