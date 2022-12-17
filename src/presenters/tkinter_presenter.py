from presenters.common import BoardPresenter

class TkInterBoardPresenter(BoardPresenter):
    def __init__(self, board, canvas, style):
        super().__init__(board)

        self.style = style
        self.canvas = canvas

    def draw(self):

        cell_width = self.canvas.winfo_width() // self.board.width
        cell_height = self.canvas.winfo_height() // self.board.height

        for i in range(self.board.width):
            for j in range(self.board.width):
                self.style.draw_cell((cell_width * i, cell_height * j, cell_width, cell_height), self.board.get_color((i, j)), self.canvas)

    def _clear(self):
        self.canvas.delete("all")