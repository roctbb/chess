import pytest

from domain.board import Board, Side

def test_white():
    board = Board(Side.WHITE)

    assert board.get((0, 2)) == None
    assert board.get((0, 1)).side == Side.BLACK
    assert board.get((2, 6)) == None
    assert board.get((7, 2)).side == Side.BLACK
    assert board.get((0, 3)) == None
    assert board.get((7, 4)) == None
    assert board.get((0, 5)).side == Side.WHITE
    assert board.get((1, 5)) == None
    assert board.get((7, 6)).side == Side.WHITE
    assert board.get((7, 7)) == None

    with pytest.raises(Exception):
        board.get((0, -1))

    with pytest.raises(Exception):
        board.get((-1, 0))

    with pytest.raises(Exception):
        board.get((8, 0))

    with pytest.raises(Exception):
        board.get((0, 8))
