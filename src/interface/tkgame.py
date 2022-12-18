from domain.common import Color
from domain.game import Game
from interface.common import GameEngine
from interface.styles import DefaultTkBoardStyle
from domain.board import Board
from domain.chess.rules import StandardChessRules
from tkinter import Tk, Canvas


class TkGame(GameEngine):
    def __init__(self):
        super().__init__()

    def run(self):
        self.window = Tk()
        self.game = Game(StandardChessRules, Color.WHITE)
        self.board = self.game.board
        self.style = DefaultTkBoardStyle()
        self._active_turn_from = None
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.window, width=640, height=640)
        self.canvas.bind("<Button-1>", self._click)
        self.canvas.pack(fill="both", expand=True)
        self.window.bind("<Configure>", self._window_resized)
        self._draw_board()

        self.window.mainloop()

    def _window_resized(self, event):
        height = event.width
        width = event.height

        if height <= 0 or width <= 0:
            return

        self._draw_board()

    def _click(self, event):
        x, y = event.x, event.y

        point = self._find_cell_coordinates(x, y)

        if not self._active_turn_from:
            if self.game.pick(point):
                self._active_turn_from = point
        else:
            self.game.move(self._active_turn_from, point)
            self._active_turn_from = None

        self._clear()
        self._draw_board()

    def _draw_board(self):
        cell_width = self.canvas.winfo_width() // self.board.width
        cell_height = self.canvas.winfo_height() // self.board.height

        if cell_width <= 1 or cell_height <= 1:
            return

        for i in range(self.board.width):
            for j in range(self.board.width):
                self.style.draw_cell((cell_width * i, cell_height * j, cell_width, cell_height),
                                     self.board.color_of((i, j)), self.canvas, self._active_turn_from == (i, j))

                if self.board.get((i, j)):
                    self.style.draw_figure((cell_width * i, cell_height * j, cell_width, cell_height),
                                           self.board.get((i, j)), self.canvas)

    def _find_cell_coordinates(self, x, y):
        cell_width = self.canvas.winfo_width() // self.board.width
        cell_height = self.canvas.winfo_height() // self.board.height

        i = x // cell_width
        j = y // cell_height

        return (i, j)

    def _clear(self):
        self.canvas.delete("all")
