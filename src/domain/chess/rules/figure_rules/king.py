from typing import List

from domain.board import Board
from domain.common import Point, Color
from domain.rules import FigureRule


class KingRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        return False
