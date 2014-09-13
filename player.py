class Player:
  def __init__(self):
    self.dead   = False
    self.room   = None
    self.items  = []
    self.x, self.y = 1, 4
    self.dx, self.dy = 0, 0
  def take(self):
    if self.room.items != []:
      for item in self.room.items:
        self.room.items.remove(item)
        self.items.append(item)
        item.taken = True
