import abc
from typing import Tuple, Optional
from domain.common import Color
from typing import TypeVar

TFigure = TypeVar("TFigure", bound="Figure")


class Figure:
    LITERAL: str = None

    def __init__(self, color: Color):
        self.color = color

    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

    def _colorise(self, s):
        if self.color == Color.WHITE:
            return s.upper()
        return s

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
