from domain.common import Color
from domain.common import Figure


class Bishop(Figure):
    LITERAL = 'b'

    # Слон
    def __init__(self, color: Color):
        super().__init__(color)
