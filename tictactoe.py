import random

from board import Board
from player import Player
from adjudicator import Adjudicator
from game_state import GameState


class TicTacToe:
  def __init__(self, player_1_strategy, player_2_strategy):
    self.adjudicator = Adjudicator()
    self.game_state = GameState()
    self.board = Board()
    self.player_list = [
      Player('1', '1', player_1_strategy),
      Player('2', '2', player_2_strategy)
    ]
    self.move_history = []

  def start(self) -> None:
    self._reset()

    while not self.game_state.game_over:
      active_player = self.player_list[self.game_state.move_count % len(self.player_list)]

      move = active_player.get_move(self.board)

      if self.board.is_valid_move(move):
        self.game_state.move_count += 1
        self.move_history.append((self.board.get_flat_string_board(), move.row * 3 + move.column))
        self.board.play_move(move)
        self.adjudicator.adjudicate(self.board, self.game_state, active_player)

  def _reset(self):
    self.game_state.reset()
    self.board.reset()
    self.move_history = []
