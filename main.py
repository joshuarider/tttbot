import strategies
from tictactoe import TicTacToe


def main():
  game = TicTacToe(strategies.RandomStrategy(), strategies.RandomStrategy())

  game.start()
  print(game.move_history)
  print(game.game_state.winner)

  print('----')

  game.start()
  print(game.move_history)
  print(game.game_state.winner)


if __name__ == '__main__':
  main()
