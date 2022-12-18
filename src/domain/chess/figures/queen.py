from domain.common import Color
from domain.common import Figure


class Queen(Figure):

    LITERAL = 'q'

    def __init__(self, color: Color):
        super().__init__(color)

    def __str__(self):
        return self._colorise(Queen.LITERAL)
