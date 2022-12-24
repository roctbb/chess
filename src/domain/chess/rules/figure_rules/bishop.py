from typing import List

from domain.board import Board
from domain.common import Point, Color
from domain.rules import FigureRule


class BishopRule(FigureRule):
    @staticmethod
    def can_move(points: List[Point], turn: Color, board: Board) -> bool:
        start, end = points

        vx = 0
        vy = 0
        figure = board.get(start)
        if not figure:
            raise Exception("Invalid move")

        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            if end[0] < start[0]:
                vx = -1
            if end[1] < start[1]:
                vy = -1
            if end[0] > start[0]:
                vx = 1
            if end[1] > start[1]:
                vy = -1

            current = (start[0] + vx, start[1] + vy)
            while current != end:
                if board.get(current) is not None:
                    return False
                current = (current[0] + vx, current[1] + vy)
            if not board.get(end) or board.get(end).color != figure.color:
                return True
        return False
