# Вот тут, как мне кажется, поплыло разделение ответственности классов: с какой стати доска что-то "знает" о фигурах?
# А если мы этот класс переделаем под нарды или шашки, то что будет? А будет нарушение базового принципа
# "можно добавлять класс, нельзя изменять класс".
from domain.common import Color, Point
from domain.common import Figure
from typing import Optional


class Board:
    def __init__(self, size: Point, orientation: Color):
        self._cells = {}
        self._size = size
        self._orientation = orientation

        self._eaten = {
            Color.WHITE: [],
            Color.BLACK: []
        }

    def load_state(self, state: str):
        rows = state.strip('\n').split()

        if len(rows) != self._size[1]:
            raise Exception("Incorrect template")

        for row in rows:
            if len(row) != self._size[0]:
                raise Exception("Incorrect template")

        for j in range(len(rows)):
            row = rows[j]
            for i in range(len(row)):
                f = row[i]
                if f == '_':
                    continue
                figure = Figure.get_by_literal(f)
                if not figure:
                    raise Exception("Incorrect literal in template: " + f)
                self.set((i, j), figure)

    @property
    def width(self) -> int:
        return self._size[0]

    @property
    def height(self) -> int:
        return self._size[1]

    @property
    def orientation(self) -> Color:
        return self._orientation

    def set(self, position: Point, figure: Optional[Figure]) -> bool:
        i, j = position

        if not self._point_available(position):
            return False

        self._cells[position] = figure
        return True

    def get(self, point: Point) -> Optional[Figure]:
        if not self._point_available(point):
            return None
        if point in self._cells:
            return self._cells[point]
        else:
            return None

    def move(self, start: Point, end: Point) -> bool:
        if not self._point_available(start) or not self._point_available(end):
            return False

        figure = self.get(start)
        if not figure:
            return False

        self.set(start, None)

        enemy = self.get(end)
        if enemy:
            self._eaten[enemy.color].append(enemy)

        self.set(end, figure)

        return True

    def color_of(self, point: Point) -> Color:
        if sum(point) % 2 == 0:
            return Color.WHITE
        else:
            return Color.BLACK

    def _point_available(self, position: Point) -> bool:
        i, j = position
        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            return False
        return True

    def get_eaten_by(self, color: Color) -> tuple:
        return tuple(self._eaten[color])

    def clear(self):
        self._cells = {}


class ImmutableBoard:
    def __init__(self, board: Board):
        self._board = board

    def get(self, point: Point) -> Optional[Figure]:
        return self._board.get(point)

    def color_of(self, point: Point) -> Color:
        return self._board.color_of(point)

    def get_eaten_by(self, color: Color) -> tuple:
        return tuple(self._board.get_eaten_by(color))

    @property
    def width(self) -> int:
        return self._board.width

    @property
    def height(self) -> int:
        return self._board.height

    @property
    def orientation(self) -> int:
        return self.orientation
