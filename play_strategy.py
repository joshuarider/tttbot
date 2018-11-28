import abc

from board import Board
from move import Move


class PlayStrategy(abc.ABC):
  @abc.abstractmethod
  def get_move(self, board: Board) -> Move:
    pass
