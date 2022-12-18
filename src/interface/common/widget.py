from tkinter import Canvas
from typing import Optional

from domain.common import Point


class Widget:
    def __init__(self, position: Point, size: Point, canvas: Canvas):
        self._canvas = canvas
        self._x = position[0]
        self._y = position[1]
        self._width = size[0]
        self._height = size[1]
        self._objects = []
        self._canvas.bind("<Button-1>", self.__click)
        self._canvas.after(1000, self.__updater)

    def move_to(self, position):
        self._x = position[0]
        self._y = position[1]

        self.redraw()

    def __updater(self):
        self.redraw()
        self._canvas.after(1000, self.__updater)

    def resize(self, size):
        self._width = size[0]
        self._height = size[1]

        self.redraw()

    def draw(self):
        raise NotImplementedError

    def redraw(self):
        self.clear()
        self.draw()

    def clear(self):
        for object in self._objects:
            self._canvas.delete(object)

    def __localize_click(self, point: Point) -> Optional[Point]:
        x, y = point
        local_x, local_y = x - self._x, y - self._y

        if local_x >= 0 and local_y >= 0 and local_x < self._width and local_y < self._height:
            return (local_x, local_y)
        return None

    def __click(self, event):
        point = self.__localize_click((event.x, event.y))
        if point:
            self._click(point)

    def _click(self, point: Point):
        pass

    def __del__(self):
        self.clear()
