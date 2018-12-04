from board import Board
from game_state import GameState
from move import Move


class Adjudicator:
  def adjudicate(self, board: Board, game_state: GameState, player_name: str) -> None:
    for line in board.get_lines():
      if self._is_a_winning_line(line):
        self._update_winning_state(game_state, player_name)
        return

    if game_state.move_count == board.DIMENSION ** 2:
        self._update_drawn_state(game_state)

  def is_winning_move(self, board: Board, move: Move, symbol: str) -> bool:
    board.rows[move.row][move.column] = symbol

    for line in board.get_lines():
      if self._is_a_winning_line(line):
        board.rows[move.row][move.column] = None
        return True

    board.rows[move.row][move.column] = None

    return False

  def _update_winning_state(self, game_state: GameState, player_name: str) -> None:
    game_state.game_over = True
    game_state.winner = player_name

  def _update_drawn_state(self, game_state: GameState) -> None:
    game_state.game_over = True
    game_state.winner = "DRAW"

  def _is_a_winning_line(self, line: list) -> bool:
    return len(set(line)) == 1 and line[0] is not None
