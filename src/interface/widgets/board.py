from domain.board import ImmutableBoard
from domain.common import Point
from interface.common import Widget
from tkinter import Canvas
from interface.styles import DefaultTkBoardStyle


class BoardWidget(Widget):
    def __init__(self, board: ImmutableBoard, point, size, style: DefaultTkBoardStyle, canvas: Canvas):
        super().__init__(point, size, canvas)

        self._board = board
        self._active_turn_from = None
        self._style = style
        self._select_callback = None

    def draw(self):
        cell_width = self._width // self._board.width
        cell_height = self._height // self._board.height

        if cell_width <= 1 or cell_height <= 1:
            return

        for i in range(self._board.width):
            for j in range(self._board.width):
                rect = (self._x + cell_width * i, self._y + cell_height * j, cell_width, cell_height)
                cell = self._style.draw_cell(rect, self._board.color_of((i, j)), self._canvas,
                                             self._active_turn_from == (i, j))
                self._objects.append(cell)

                if self._board.get((i, j)):
                    figure = self._style.draw_figure(
                        (self._x + cell_width * i, self._y + cell_height * j, cell_width, cell_height),
                        self._board.get((i, j)), self._canvas)
                    self._objects.append(figure)

    def pick(self, point: Point):
        self._active_turn_from = point
        self.redraw()

    def unpick(self):
        self._active_turn_from = None
        self.redraw()

    def on_select(self, callback):
        self._select_callback = callback

    def __find_cell_coordinates(self, point):
        x, y = point
        cell_width = self._width // self._board.width
        cell_height = self._height // self._board.height

        i = x // cell_width
        j = y // cell_height

        return (i, j)

    def _click(self, point: Point):
        i, j = self.__find_cell_coordinates(point)

        if self._select_callback:
            self._select_callback((i, j))
