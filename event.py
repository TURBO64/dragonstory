class Event:
  def __init__(self, trigger, outcome, descr):
    self.trigger = trigger
    self.outcome = outcome
    self.descr = descr
    self.flag = False