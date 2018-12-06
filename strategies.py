import os
import abc

import pickle
import numpy as np

from board import Board
from move import Move
from adjudicator import Adjudicator


class PlayStrategy(abc.ABC):
  @abc.abstractmethod
  def get_move(self, board: Board) -> Move:
    pass

  @abc.abstractmethod
  def clean_up(self):
    pass


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

  #FIXME interface segregation
  def clean_up(self):
    pass

class RandomStrategy(PlayStrategy):
  def get_move(self, board: Board) -> Move:
    return Move(
      np.random.randint(0, board.DIMENSION),
      np.random.randint(0, board.DIMENSION)
    )

  #FIXME interface segregation
  def clean_up(self):
    pass

class GoFirstQTableStrategy(PlayStrategy):
  EXPERIENCE_FILE = 'go_first_strategy.pickle'
  NOISE_LEVEL = 0.02
  LEARNING_RATE = 0.5
  DISCOUNT_RATE = 0.95
  REWARDS = {
    'win' : 1.,
    'draw' : 0.5,
  }

  def __init__(self):
    self.mini_judge = Adjudicator()
    self.Q = {}
    if os.path.isfile(GoFirstQTableStrategy.EXPERIENCE_FILE):
      with open(GoFirstQTableStrategy.EXPERIENCE_FILE, 'rb') as handle:
        self.Q = pickle.load(handle)

  def get_move(self, board: Board) -> Move:
    flat_board = board.flatten()

    if flat_board not in self.Q:
      self.Q[flat_board] = np.zeros(9)

    open_spaces = [(i, self.Q[flat_board][i] + np.random.randn() * GoFirstQTableStrategy.NOISE_LEVEL) for i, char in enumerate(flat_board) if char == '0']

    chosen_move_index, _ = max(open_spaces, key=lambda item: item[1])

    row, column = divmod(chosen_move_index, 3)
    move = Move(row, column)
    updated_flat_board = ''.join(flat_board[:chosen_move_index] + '1' + flat_board[chosen_move_index + 1:])

    reward = self._get_reward(board, move)

    if reward not in GoFirstQTableStrategy.REWARDS.values():
      updated_flat_board = self._add_best_enemy_move_to_flat_board(updated_flat_board)

    self.Q[flat_board][chosen_move_index] = self.Q[flat_board][chosen_move_index] + self.LEARNING_RATE * (reward + self.DISCOUNT_RATE * np.max(self._get_possibilities(updated_flat_board)) - self.Q[flat_board][chosen_move_index])

    return move

  def clean_up(self):
    with open(GoFirstQTableStrategy.EXPERIENCE_FILE, 'wb') as storage_file:
      pickle.dump(self.Q, storage_file, protocol=pickle.HIGHEST_PROTOCOL)

  def _add_best_enemy_move_to_flat_board(self, flat_board: str) -> str:
    open_spaces = [(i, self._get_possibilities(flat_board)[i] + np.random.randn() * GoFirstQTableStrategy.NOISE_LEVEL) for i, char in enumerate(flat_board) if char == '0']

    if not open_spaces:
      return flat_board

    chosen_move_index, _ = min(open_spaces, key=lambda item:item[1])

    return flat_board[:chosen_move_index] + '2' + flat_board[chosen_move_index + 1:]

  def _get_possibilities(self, flat_board):
    if flat_board not in self.Q:
      self.Q[flat_board] = np.zeros(9)

    return self.Q[flat_board]

  def _get_reward(self, board: Board, move: Move) -> int:
    if self.mini_judge.is_winning_move(board, move, '1'):
      return GoFirstQTableStrategy.REWARDS['win']
    elif len([1 for row in board.rows for item in row if item is None]) == 1:
      return GoFirstQTableStrategy.REWARDS['draw']

    return 0
