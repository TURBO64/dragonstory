class Room:
  def __init__(self, name, x, y, items, events, descr):
    self.name = name
    self.x, self.y = x, y
    self.items = items
    self.events = events
    self.descr = descr
  def run_events(self):
    for x in events:
      if x.flag == False:
        x.trigger()
