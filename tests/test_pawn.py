import pytest

from domain.board import Board, Side


def test_initial_step():
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

    expected = """
rhbqkbhr
pppppppp
________
________
P_______
________
_PPPPPPP
RHBQKBHR
"""

    assert board.get_state().strip('\n') == expected.strip('\n')

def test_cant_step_back():
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

def test_cannot_double_step():
    board = Board(Side.WHITE)
    board.move((0, 6), (0, 4))
    assert board.move((0, 4), (0, 2)) == False

def test_cant_eat_forward():
    initial = """
rhbqkbhr
pppppppp
P_______
________
________
________
_PPPPPPP
RHBQKBHR
"""

    board = Board(Side.WHITE, initial)

    assert board.move((0, 2), (0, 1)) == False


def test_can_eat_diag():
    initial = """
rhbqkbhr
pppppppp
P_______
________
________
________
_PPPPPPP
RHBQKBHR
"""

    board = Board(Side.WHITE, initial)

    assert board.move((0, 2), (1, 1)) == True
    assert len(board.eaten[Side.BLACK]) == 1

def test_can_eat_diag_back():
    initial = """
rhbqkbhr
p_pppppp
P_______
_p______
________
________
_PPPPPPP
RHBQKBHR
"""

    board = Board(Side.WHITE, initial)

    assert board.move((0, 2), (1, 3)) == True
    assert len(board.eaten[Side.BLACK]) == 1