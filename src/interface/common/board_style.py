import abc

class TkBoardStyle:
    def __init__(self):
        pass

    @staticmethod
    def draw_cell(rect, color, canvas):
        raise NotImplementedError

    @staticmethod
    def draw_figure(rect, figure, canvas):
        raise NotImplementedError