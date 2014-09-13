class Game:
  def __init__(self):
    self.end   = False
    self.moves = 0
    self.currentroom = room_start
  def goto(self, room):
    self.currentroom = room
    self.look()
  def look(self):
    io.cout(self.currentroom.name, io.white)
    io.cout(textwrap.dedent(textwrap.fill(self.currentroom.descr)) + "\n")
    io.cout("Obvious exits: ")
  #def move(self, dir):
    #if self.currentroom.checkexit(dir) == 1: