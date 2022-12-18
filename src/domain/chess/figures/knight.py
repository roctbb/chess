from domain.common import Color
from domain.common import Figure


class Knight(Figure):
    # Конь

    LITERAL = 'n'

    def __init__(self, color: Color):
        super().__init__(color)

    def __str__(self):
        return self._colorise(Knight.LITERAL)  # В шахматной нотации Конь это не "Horse", а N, от kNight