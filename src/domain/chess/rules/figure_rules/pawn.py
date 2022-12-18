from domain.common import FigureRule, Point, Color
from domain.board import Board


class PawnRule(FigureRule):
    @staticmethod
    def can_move(start: Point, end: Point, turn: Color, board: Board) -> bool:
        figure = board.get(start)
        if not figure:
            raise Exception("Invalid move")

        direction = -1 if turn == board.orientation else 1
        first_move = (start[1] == 6 and figure.color == board.orientation) or (
                    start[1] == 1 and figure.color != board.orientation)

        # прямой ход
        if start[0] == end[0]:
            if end[1] == start[1] + direction and board.get(end) is None:
                return True
            if end[1] == start[1] + 2 * direction and board.get(end) is None and board.get(
                    (start[0], start[1] + direction)) is None and first_move:
                return True
        # косой ход
        if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 1:
            if board.get(end) is not None and board.get(end).color != figure.color:
                return True

        return False
