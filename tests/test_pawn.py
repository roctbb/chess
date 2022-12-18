from domain.common import Color
from domain.board import Board
from domain.chess.rules import ChessRules


def test_initial_step():
    initial = """
rnbqkbnr
pppppppp
________
________
________
________
PPPPPPPP
RNBQKBNR
"""

    board = Board((8, 8), Color.WHITE)
    board.load_state(initial)

    board.move((0, 6), (0, 4))

    expected = """
rnbqkbnr
pppppppp
________
________
P_______
________
_PPPPPPP
RNBQKBNR
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

    board = Board(Color.WHITE, initial)
    assert board.move((0, 3), (0, 4)) == False

def test_cannot_double_step():
    board = Board(Color.WHITE)
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

    board = Board(Color.WHITE, initial)

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

    board = Board(Color.WHITE, initial)

    assert board.move((0, 2), (1, 1)) == True
    assert len(board.eaten[Color.BLACK]) == 1

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

    board = Board(Color.WHITE, initial)

    assert board.move((0, 2), (1, 3)) == True
    assert len(board.eaten[Color.BLACK]) == 1