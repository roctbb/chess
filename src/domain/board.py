from typing import Optional, Tuple
from domain.figures import *
from domain.common import Side


class Board:
    def __init__(self, side: Side = Side.WHITE):
        self._cells = {}
        self._size = (8, 8)
        self.score = {
            side: 0,
            Side.opposite(side): 0
        }
        self.side = side

        self.__place_row((0, 6), [Pawn] * 8, side)
        self.__place_row((0, 7), [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], side)
        self.__place_row((0, 1), [Pawn] * 8, side)
        self.__place_row((0, 0), [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook], side)

    def __set(self, position, figure):
        i, j = position

        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            raise Exception("Outside of field")

        self._cells[position] = figure

    def __is_black(self, point):
        i, j = point
        return (i + j) % 2 == 1

    def __place_row(self, start, figures, side):
        for i in range(start[0], start[0] + len(figures)):
            figure = figures.pop()
            self.__set((i, start[1]), figure(side))

    def point_available(self, point):
        i, j = point
        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            return False
        return True

    def get(self, point) -> Optional[Figure]:
        if not self.point_available(point):
            raise Exception("Point is outside of filed")
        if point in self._cells:
            return self._cells[point]
        else:
            return None
    # ход может состоять из нескольких клеток
    # результаты: нельзя, ход незавершен, ход завершен
    def move(self, start, end):
        if not self.point_available(start) or not self.point_available(end):
            return False

        figure = self.get(start)
        if not figure:
            return False

        attacked_points = figure.move(start, end, self)
        if attacked_points is None:
            return False

        self.__set(start, None)

        for point in attacked_points:
            self.__set(point, None)
            self.score[side] += 1

        self.__set(end, figure)

    def __repr__(self):
        print()
        for j in range(self.height):
            for i in range(self.width):
                figure = ' ' if not self.get(i, j) else self.get(i, j)
                print(figure, '|', end='')
            print()
            print('---' * self.width)

    @property
    def width(self):
        return self._size[0]

    @property
    def height(self):
        return self._size[1]
