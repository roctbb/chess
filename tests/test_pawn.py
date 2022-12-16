import pytest

from domain.board import Board, Side


def test_step():
    initial = """rhbqkbhr
pppppppp




PPPPPPPP
RHBQKBHR
        """

    board = Board(Side.WHITE, initial)
    board.move((0, 6), (0, 4))
    board.move((0, 4), (0, 3))

    expected = """rhbqkbhr
pppppppp
        
P       
        
        
 PPPPPPP
RHBQKBHR
"""

    assert board.__repr__() == expected
