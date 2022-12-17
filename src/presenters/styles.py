from presenters.common import TkBoardStyle
from domain.common import Side

class DefaultTkBoardStyle(TkBoardStyle):
    def __init__(self):
        super().__init__()

    @staticmethod
    def draw_cell(self, rect, side, canvas):
        x, y, width, height = rect

        if side == Side.WHITE:
            color = "white"
        else:
            color = "black"

        canvas.create_rectangle(x, y, x + width, y + height, color=color)

    @staticmethod
    def draw_figure(self, rect, figure, canvas):
        pass