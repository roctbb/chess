from tkinter import Canvas
from domain.chess.figures import Pawn, Rook, Bishop, Knight, Queen, King
from interface.common import TkBoardStyle
from domain.common import Color, Figure
from PIL import Image, ImageTk

class DefaultTkBoardStyle(TkBoardStyle):
    def __init__(self):
        super().__init__()


        self._images = {
            # @TODO: Вот эту сранину надо как-то изящнее сделать:
            Bishop(Color.BLACK).__str__(): Image.open("./assets/default/black_bishop.png"),
            Rook(Color.BLACK).__str__(): Image.open("./assets/default/black_rook.png"),
            Knight(Color.BLACK).__str__(): Image.open("./assets/default/black_knight.png"),
            King(Color.BLACK).__str__(): Image.open("./assets/default/black_king.png"),
            Queen(Color.BLACK).__str__(): Image.open("./assets/default/black_queen.png"),
            Pawn(Color.BLACK).__str__(): Image.open("./assets/default/black_pawn.png"),
            Bishop(Color.WHITE).__str__(): Image.open("./assets/default/white_bishop.png"),
            Rook(Color.WHITE).__str__(): Image.open("./assets/default/white_rook.png"),
            Knight(Color.WHITE).__str__(): Image.open("./assets/default/white_knight.png"),
            King(Color.WHITE).__str__(): Image.open("./assets/default/white_king.png"),
            Queen(Color.WHITE).__str__(): Image.open("./assets/default/white_queen.png"),
            Pawn(Color.WHITE).__str__(): Image.open("./assets/default/white_pawn.png")
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
        s = figure.__str__()

        image = self._images[s].resize((width, height), Image.LANCZOS)
        self._cache[(x, y)] = ImageTk.PhotoImage(image)
        canvas.create_image(x, y, image=self._cache[(x, y)], anchor="nw")