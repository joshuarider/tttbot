from board import Board
from move import Move
from play_strategy import PlayStrategy

class HumanStrategy(PlayStrategy):
  def get_move(self, board: Board) -> Move:
    row_input = self._get_move_input('Which row? ', board.DIMENSION)
    column_input = self._get_move_input('Which column? ', board.DIMENSION)

    return Move(row_input - 1, column_input - 1)

  def _get_move_input(self, prompt: str, maximum_input: int) -> None:
    try:
      move_input_raw = input(prompt)
      move_input_int = int(move_input_raw)

      if 1 <= move_input_int <= maximum_input:
        return move_input_int

      return self._get_move_input(prompt, maximum_input)
    except ValueError as e:
      return self._get_move_input(prompt, maximum_input)
