from interface.common import GameEngine
from interface.styles import DefaultTkBoardStyle
from domain.board import Board
from tkinter import Tk, Canvas

class TkGame(GameEngine):
    def __init__(self):
        super().__init__()

    def run(self):
        self.window = Tk()
        self.board = Board()
        self.style = DefaultTkBoardStyle()
        self._active_turn_from = None

        self.window.resizable(width=False, height=False)
        self.canvas = Canvas(self.window, width=640, height=640)
        self.canvas.bind("<Button-1>", self._click)
        self.canvas.pack()

        self._draw_board()

        self.window.mainloop()

    def _click(self, event):
        x, y = event.x, event.y

        point = self._find_cell_coordinates(x, y)
        figure = self.board.get(point)

        if not self._active_turn_from:
            if not figure:
                return

            if figure.color != self.board.get_current_turn():
                return

            self._active_turn_from = point
        else:
            self.board.move(self._active_turn_from, point)
            self._active_turn_from = False

        self._clear()
        self._draw_board()

    def _draw_board(self):
        cell_width = int(self.canvas['width']) // self.board.width
        cell_height = int(self.canvas['height']) // self.board.height

        for i in range(self.board.width):
            for j in range(self.board.width):
                self.style.draw_cell((cell_width * i, cell_height * j, cell_width, cell_height), self.board.get_color((i, j)), self.canvas, self._active_turn_from == (i, j))

                if self.board.get((i, j)):
                    self.style.draw_figure((cell_width * i, cell_height * j, cell_width, cell_height), self.board.get((i, j)), self.canvas)

    def _find_cell_coordinates(self, x, y):
        cell_width = int(self.canvas['width']) // self.board.width
        cell_height = int(self.canvas['height']) // self.board.height

        i = x // cell_height
        j = y // cell_height

        return (i, j)

    def _clear(self):
        self.canvas.delete("all")
