import os

from board import Board
from game_state import GameState


class ViewScreen:
  def print_board(self, board: Board) -> None:
    os.system('clear')

    for row in board.rows:
      print(' '.join([x if x else ' ' for x in row]))

  def announce_outcome(self, game_state: GameState) -> None:
    if not game_state.winner:
      print('Draw! Everyone is equally good!')
      return

    print('Congratulations, {}!'.format(game_state.winner))
