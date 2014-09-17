class Player:
  def __init__(self):
    self.dead   = False
    self.room   = None
    self.items  = []
    self.x, self.y = 1, 4
    self.dx, self.dy = 0, 0