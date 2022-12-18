from domain.common import Color
from domain.common import Figure


class Pawn(Figure):
    LITERAL = 'p'

    def __init__(self, color: Color):
        super().__init__(color)
