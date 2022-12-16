import pytest

from domain.board import Board, Side


def test_step():
    initial = """
rhbqkbhr
pppppppp
________
________
________
________
PPPPPPPP
RHBQKBHR
"""

    board = Board(Side.WHITE, initial)
    board.move((0, 6), (0, 4))
    board.move((0, 4), (0, 3))

    expected = """
rhbqkbhr
pppppppp
________
P_______
________
________
_PPPPPPP
RHBQKBHR
"""

    assert board.__repr__().strip('\n') == expected.strip('\n')
