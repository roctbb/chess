from tkinter import Canvas

from domain.figures import Figure
from interface.common import TkBoardStyle
from domain.common import Color
from PIL import Image, ImageTk

class DefaultTkBoardStyle(TkBoardStyle):
    def __init__(self):
        super().__init__()

        self._images = {
            'b': Image.open("./assets/default/black_bishop.png"),
            'r': Image.open("./assets/default/black_rook.png"),
            'h': Image.open("./assets/default/black_knight.png"),
            'k': Image.open("./assets/default/black_king.png"),
            'q': Image.open("./assets/default/black_queen.png"),
            'p': Image.open("./assets/default/black_pawn.png"),
            'B': Image.open("./assets/default/white_bishop.png"),
            'R': Image.open("./assets/default/white_rook.png"),
            'H': Image.open("./assets/default/white_knight.png"),
            'K': Image.open("./assets/default/white_king.png"),
            'Q': Image.open("./assets/default/white_queen.png"),
            'P': Image.open("./assets/default/white_pawn.png")
        }
        self._cache = {}


    def draw_cell(self, rect, color, canvas: Canvas, active=False):
        x, y, width, height = rect

        if active:
            color = "yellow"
        elif color == Color.WHITE:
            color = "white"
        else:
            color = "black"
        canvas.create_rectangle(x, y, x + width, y + height, fill=color)

    def draw_figure(self, rect, figure: Figure, canvas):
        x, y, width, height = rect
        x += width // 5
        y += height // 5
        width -= 2 * width // 5
        height -= 2 * height // 5
        s = figure.__repr__()

        image = self._images[s].resize((width, height), Image.LANCZOS)
        self._cache[(x, y)] = ImageTk.PhotoImage(image)
        canvas.create_image(x, y, image=self._cache[(x, y)], anchor="nw")