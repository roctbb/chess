import abc


class GameEngine:
    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        raise NotImplementedError