from domain.common import Color
from domain.common import Figure


class King(Figure):
    LITERAL = 'k'

    def __init__(self, color: Color):
        super().__init__(color)
