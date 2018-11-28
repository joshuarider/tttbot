import pickle
import numpy as np

import strategies
from tictactoe import TicTacToe


def main():
  try:
    with open('random_results.pickle', 'rb') as handle:
      Q = pickle.load(handle)
  except IOError:
    Q = {}

  lr = 0.8
  y = 0.95
  episodes = 2000

  game = TicTacToe(strategies.RandomStrategy(), strategies.RandomStrategy())
  game_ratings = {
    '1' : 1,
    '2' : -1,
    'DRAW' : 0
  }

  for i in range(episodes):
    game.start()

    final_board, final_move = game.move_history[-1]

    if final_board not in Q:
      Q[final_board] = np.zeros(9)

    Q[final_board][final_move] += int(game_ratings[game.game_state.winner])

  for key, vals in Q.items():
    print('{} - {}'.format(key, vals))
  print(len(Q))
  with open('random_results.pickle', 'wb') as storage_file:
    pickle.dump(Q, storage_file, protocol=pickle.HIGHEST_PROTOCOL)
if __name__ == '__main__':
  main()
