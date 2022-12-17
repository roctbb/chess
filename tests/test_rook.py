import pytest
from domain.board import Board, Side

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

    board = Board(Side.WHITE, initial)
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

    board = Board(Side.WHITE, initial)
    assert board.move((0, 8), (0, 5)) == True