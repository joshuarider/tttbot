from move import Move


class Board:
  DIMENSION = 3

  def __init__(self):
    self._initialise()

  def is_valid_move(self, move: Move) -> bool:
    return self.rows[move.row][move.column] == None

  def play_move(self, move: Move) -> bool:
    if not self.is_valid_move(move):
      return False

    self.rows[move.row][move.column] = move.value
    self.move_list.append(move.row * 3 + move.column)

    return True

  def get_lines(self) -> list:
    # FIXME sacrificing too much readability?
    return (self.rows # rows
      + [[self.rows[row][column] for row in range(self.DIMENSION)] for column in range(self.DIMENSION)] # columns
      + [[self.rows[i][i] for i in range(self.DIMENSION)]] # top-left to bottom-right diagonal
      + [[self.rows[i][self.DIMENSION - i - 1] for i in range(self.DIMENSION)]] # top-right to bottom-left diagonal
      )

  def reset(self):
    self._initialise()

  def _initialise(self):
    self.rows = [[None for i in range(self.DIMENSION)] for j in range(self.DIMENSION)]
    self.move_list = []

  def flatten(self):
    return ''.join(
      [str(space) if space else '0' for row in self.rows for space in row]
    )
