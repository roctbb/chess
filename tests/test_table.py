import pytest

from domain.board import Board, Side


def test_white():
    board = Board(Side.WHITE)

    expected = """
rhbqkbhr
pppppppp
________
________
________
________
PPPPPPPP
RHBQKBHR
"""

    assert board.get_state().strip('\n') == expected.strip('\n')

    with pytest.raises(Exception):
        board.get((0, -1))

    with pytest.raises(Exception):
        board.get((-1, 0))

    with pytest.raises(Exception):
        board.get((8, 0))

    with pytest.raises(Exception):
        board.get((0, 8))


def test_black():
    board = Board(Side.BLACK)

    expected = """
RHBKQBHR
PPPPPPPP
________
________
________
________
pppppppp
rhbkqbhr
"""
    assert board.get_state().strip('\n') == expected.strip('\n')

    with pytest.raises(Exception):
        board.get((0, -1))

    with pytest.raises(Exception):
        board.get((-1, 0))

    with pytest.raises(Exception):
        board.get((8, 0))

    with pytest.raises(Exception):
        board.get((0, 8))

def test_sequental_moves():
    board = Board(Side.WHITE)
    assert board.move((0, 6), (0, 5)) == True
    assert board.move((0, 5), (0, 4)) == False
    assert board.move((0, 1), (0, 2)) == True
    assert board.move((0, 2), (0, 3)) == False
    assert board.move((0, 5), (0, 4)) == True