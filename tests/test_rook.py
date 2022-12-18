from domain.board import Board
from domain.common import Color

def test_close():
    initial = """
rhbqkbhr
pppppppp
________
P_______
________
________
_PPPPPPP
RHBQKBHR
"""

    board = Board(Color.WHITE, initial)
    assert board.move((0, 3), (0, 4)) == False

def test_dia():
    initial = """
rhbqkbhr
pppppppp
________
P_______
________
________
_PPPPPPP
RHBQKBHR
"""

    board = Board(Color.WHITE, initial)
    assert board.move((0, 8), (0, 5)) == True