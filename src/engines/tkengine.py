from engines.common import GameEngine
from presenters.tkinter_presenter import TkInterBoardPresenter
from presenters.styles import DefaultTkBoardStyle
from domain.board import Board
from tkinter import Tk, Canvas

class TkGameEngine(GameEngine):
    def __init__(self):
        super().__init__()

    def run(self):
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.canvas = Canvas(self.window, width=640, height=640)
        self.board = Board()

        self.presenter = TkInterBoardPresenter(self.board, self.canvas, DefaultTkBoardStyle)

        self.window.mainloop()

    def _click(self, event):
        pass
