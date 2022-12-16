from enum import Enum

class Side(Enum):
    WHITE = 1
    BLACK = 0

    @staticmethod
    def opposite(side):
        return Side.BLACK if side == Side.WHITE else Side.WHITE