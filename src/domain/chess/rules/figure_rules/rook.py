from typing import List

from domain.board import Board
from domain.common import FigureRule, Point, Color


class RookRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        start, end = points
        if start[0] == end[0]:
            if start[1] > end[1]:
                for i in range(end[1] + 1, start[1]):
                    if board.get((start[0], i)) is not None:
                        return False
            elif start[1] < end[1]:
                for i in range(start[1], end[1] - 1):
                    if board.get((start[0], i)) is not None:
                        return False
            return True
        elif start[1] == end[1]:
            if start[0] > end[0]:
                for i in range(end[0] + 1, start[0]):
                    if board.get((start[1], i)) is not None:
                        return False
            elif start[0] < end[0]:
                for i in range(start[0], end[0] - 1):
                    if board.get((start[1], i)) is not None:
                        return False
            return True
        return False
