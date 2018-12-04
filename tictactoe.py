import random

from board import Board
from adjudicator import Adjudicator
from game_state import GameState


class TicTacToe:
  def __init__(self, player_list):
    self.adjudicator = Adjudicator()
    self.game_state = GameState()
    self.board = Board()
    self.player_list = player_list

  def start(self) -> None:
    self._reset()

    while not self.game_state.game_over:
      active_player = self.player_list[self.game_state.move_count % len(self.player_list)]

      move = active_player.get_move(self.board)

      if self.board.is_valid_move(move):
        self.game_state.move_count += 1
        self.board.play_move(move)
        self.adjudicator.adjudicate(self.board, self.game_state, active_player.name)

  def _reset(self):
    self.game_state.reset()
    self.board.reset()
    self.move_history = []
