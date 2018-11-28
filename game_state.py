class GameState:
  def __init__(self):
    self._initialise()

  def reset(self) -> None:
    self._initialise()

  def _initialise(self) -> None:
    self.move_count = 0
    self.game_over = False
    self.winner = None
