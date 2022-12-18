from domain.common import Color
from domain.game import Game
from interface.common import GameEngine
from interface.styles import DefaultTkBoardStyle
from domain.chess.rules import StandardChessRules
from tkinter import Tk, Canvas
from interface.widgets import BoardWidget
from domain.chess.players import DummyPlayer, GuiPlayer


class TkGame(GameEngine):
    def __init__(self):
        super().__init__()

    def run(self):
        self.window = Tk()
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.window, width=640, height=640)
        self.canvas.pack(fill="both", expand=True)

        self.window.bind("<Configure>", self._window_resized)

        self.game = Game(StandardChessRules, Color.WHITE)
        self.player1 = GuiPlayer(self.game, Color.WHITE)
        self.player2 = GuiPlayer(self.game, Color.BLACK)

        self.board_widget = BoardWidget(self.game.board, (0, 0), (640, 640), DefaultTkBoardStyle(), self.canvas)
        self.board_widget.subscribe(self.player1)
        self.board_widget.subscribe(self.player2)

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
