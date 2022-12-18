from domain.common import Color
from domain.common import Figure


class Rook(Figure):

    LITERAL = 'r'

    # Ладья
    def __init__(self, color: Color):
        super().__init__(color)

    def __str__(self):
        return self._colorise(Rook.LITERAL)