import strategies
from player import Player
from tictactoe import TicTacToe
from adjudicator import Adjudicator


def main():
  player_1 = Player('1', '1', strategies.GoFirstQTableStrategy(Adjudicator()))
  player_list = [
      player_1,
      Player('2', '2', strategies.RandomStrategy())
  ]
  game = TicTacToe(player_list)

  episodes = 100000

  for i in range(episodes):
    game.start()
    print(game.game_state.winner)
    # if game.game_state.winner == '2':
    #   print(' --- GAME {} ---'.format(i))
    #   print(game.board.flatten())
    #   for move in game.board.move_list:
    #     print(move)

  player_1.clean_up()

if __name__ == '__main__':
  main()
