from domain.common import Color
from domain.game import Game
from interface.common import GameEngine
from interface.styles import DefaultTkBoardStyle
from domain.board import Board
from domain.chess.rules import StandardChessRules
from tkinter import Tk, Canvas
from interface.widgets import BoardWidget


class TkGame(GameEngine):
    def __init__(self):
        super().__init__()

    def run(self):
        self.window = Tk()
        self.game = Game(StandardChessRules, Color.WHITE)
        self.board = self.game.board
        self.style = DefaultTkBoardStyle()

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.window, width=640, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.window.bind("<Configure>", self._window_resized)

        self.board_widget = BoardWidget(self.board, (0, 0), (640, 640), DefaultTkBoardStyle(), self.canvas)
        self.board_widget.on_select(self._pick)

        self.turn_from = None

        self.window.mainloop()

    def _window_resized(self, event):
        width = event.width
        height = event.height

        if height <= 0 or width <= 0:
            return

        if width > height:
            offset = (width - height) // 2
            self.board_widget.move_to((offset, 0))
            self.board_widget.resize((height, height))
        else:
            offset = (height - width) // 2
            self.board_widget.move_to((0, offset))
            self.board_widget.resize((width, width))

    def _pick(self, point):

        if not self.turn_from:
            if self.game.pick(point):
                self.board_widget.pick(point)
                self.turn_from = point
        else:
            print(self.turn_from, point)
            self.game.move(self.turn_from, point)
            self.turn_from = None
            self.board_widget.unpick()

