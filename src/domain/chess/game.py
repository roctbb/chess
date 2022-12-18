from domain.board import Board, ImmutableBoard
from domain.chess.rules import ChessRules
from domain.common import Color
from typing import Type
from domain.game import Game


class ChessGame(Game):
    def __init__(self, rules: Type[ChessRules], side: Color):
        super().__init__(rules, side)

    def is_check_for(self, color: Color) -> bool:
        return self._rules.check(self._board, color)

    def is_mate_for(self, color: Color) -> bool:
        return self._rules.mate(self._board, color)

    def is_over(self) -> bool:
        return self.is_mate_for(Color.WHITE) or self.is_mate_for(Color.BLACK)
