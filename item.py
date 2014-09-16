class Item:
  def __init__(self, name, pickup, descr):
    self.name   = name
    self.descr  = descr
    self.pickup = pickup
    self.taken  = False
