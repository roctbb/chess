import abc

from domain.common import Point, Color
from domain.board import Board


class FigureRule:
    @staticmethod
    @abc.abstractmethod
    def can_move(start: Point, end: Point, turn: Color, board: Board) -> bool:
        raise NotImplementedError


class GameRules:

    @staticmethod
    @abc.abstractmethod
    def can_pick(point: Point, turn: Color, board: Board) -> bool:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def can_move(start: Point, end: Point, turn: Color, board: Board) -> bool:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def moved(start: Point, end: Point, turn: Color, board: Board) -> bool:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def place_figures(board: Board, color: Color) -> bool:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def is_over(turn: Color, board: Board):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def get_first_turn():
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def get_size():
        raise NotImplementedError
