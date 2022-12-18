from typing import Optional
from typing import TypeVar

from domain.common import Color

TFigure = TypeVar("TFigure", bound="Figure")


class Figure:
    LITERAL: str = None

    def __init__(self, color: Color):
        self.color = color

    def __str__(self):
        return self._colorise(self.LITERAL)

    def _colorise(self, literal):
        if self.color == Color.WHITE:
            return literal.upper()
        return literal

    @staticmethod
    def _color_for_literal(literal: str) -> Color:
        if literal.isupper():
            return Color.WHITE
        else:
            return Color.BLACK

    @classmethod
    def get_by_literal(cls, figure_literal: str) -> Optional[TFigure]:
        subs = cls.__subclasses__()
        try:
            figure_cls = next(sub for sub in subs if sub.LITERAL == figure_literal.lower())
        except:
            return None

        return figure_cls(cls._color_for_literal(figure_literal))
