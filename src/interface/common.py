import abc


class GameEngine:
    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError

class TkBoardStyle:
    def __init__(self):
        pass

    @staticmethod
    def draw_cell(rect, color, canvas):
        raise NotImplementedError

    @staticmethod
    def draw_figure(rect, figure, canvas):
        raise NotImplementedError
