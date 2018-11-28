from board import Board
from game_state import GameState
from player import Player


class Adjudicator:
  def adjudicate(self, board: Board, game_state: GameState, player: Player) -> None:
    for line in board.get_lines():
      if self._is_a_winning_line(line):
        self._update_winning_state(game_state, player)
        return

    if game_state.move_count == board.DIMENSION ** 2:
        self._update_drawn_state(game_state)

  def _update_winning_state(self, game_state: GameState, player: Player) -> None:
    game_state.game_over = True
    game_state.winner = player.name

  def _update_drawn_state(self, game_state: GameState) -> None:
    game_state.game_over = True

  def _is_a_winning_line(self, line: list) -> bool:
    return len(set(line)) == 1 and line[0] is not None
