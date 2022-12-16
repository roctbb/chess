import pytest

from domain.board import Board, Side


def test_white():
    board = Board(Side.WHITE)

    expected = """rhbqkbhr
pppppppp
        
        
        
        
PPPPPPPP
RHBQKBHR
"""

    assert board.__repr__() == expected

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

    expected = """RHBKQBHR
PPPPPPPP
        
        
        
        
pppppppp
rhbkqbhr
"""
    assert board.__repr__() == expected

    with pytest.raises(Exception):
        board.get((0, -1))

    with pytest.raises(Exception):
        board.get((-1, 0))

    with pytest.raises(Exception):
        board.get((8, 0))

    with pytest.raises(Exception):
        board.get((0, 8))
