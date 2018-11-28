import random

from board import Board
from player import Player
from adjudicator import Adjudicator
from view_screen import ViewScreen
from game_state import GameState
from human_strategy import HumanStrategy
from random_strategy import RandomStrategy


class TicTacToe:
  def __init__(self):
    self.view_screen = ViewScreen()
    self.adjudicator = Adjudicator()

  def start(self) -> None:
    player_list = [
      Player('Player 1', 'X', HumanStrategy()),
      Player('Player 2', 'O', RandomStrategy())
    ]

    random.shuffle(player_list)

    board = Board()
    game_state = GameState()

    while not game_state.game_over:
      self.view_screen.print_board(board)

      active_player = player_list[game_state.move_count % len(player_list)]

      print("{}'s turn.".format(active_player.name))

      move = active_player.get_move(board)

      if board.play_move(move):
        game_state.move_count += 1
        self.adjudicator.adjudicate(board, game_state, active_player)

    self.view_screen.print_board(board)
    self.view_screen.announce_outcome(game_state)
