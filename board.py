from move import Move


class Board:
  DIMENSION = 3

  def __init__(self):
    self.rows = [[None for i in range(self.DIMENSION)] for j in range(self.DIMENSION)]

  def play_move(self, move: Move) -> bool:
    if self.rows[move.row][move.column] is not None:
      return False

    self.rows[move.row][move.column] = move.value

    return True

  def get_lines(self) -> list:
    # FIXME sacrificing too much readability?
    return (self.rows # rows
      + [[self.rows[row][column] for row in range(self.DIMENSION)] for column in range(self.DIMENSION)] # columns
      + [[self.rows[i][i] for i in range(self.DIMENSION)]] # top-left to bottom-right diagonal
      + [[self.rows[i][self.DIMENSION - i - 1] for i in range(self.DIMENSION)]] # top-right to bottom-left diagonal
      )
