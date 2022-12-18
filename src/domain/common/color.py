from enum import Enum

class Color(Enum):
    WHITE = 1
    BLACK = 0

    @staticmethod
    def opposite(color):
        return Color.BLACK if color == Color.WHITE else Color.WHITE