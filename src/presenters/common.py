import abc


class BoardPresenter:
    def __init__(self, board):
        self.board = board

    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError


class TkBoardStyle:
    def __init__(self):
        pass

    @abc.abstractmethod
    @staticmethod
    def draw_cell(self, rect, side, canvas):
        raise NotImplementedError

    @abc.abstractmethod
    @staticmethod
    def draw_figure(self, rect, figure, canvas):
        raise NotImplementedError
