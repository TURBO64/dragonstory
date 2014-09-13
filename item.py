class Item:
  def __init__(self, name, descr, carry):
    self.name   = name
    self.descr  = descr
    self.carry  = carry
    self.taken  = False