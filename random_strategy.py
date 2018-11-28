from random import randint

from board import Board
from move import Move
from play_strategy import PlayStrategy

class RandomStrategy(PlayStrategy):
  def get_move(self, board: Board) -> Move:
    return Move(
      randint(0, board.DIMENSION - 1),
      randint(0, board.DIMENSION - 1)
    )
