class Event:
  def __init__(self, trigger, outcome, solutions, interactive, descr, win, lose):
    self.trigger = trigger
    self.outcome = outcome
    self.solutions = solutions
    self.interactive = interactive
    self.descr = descr
    self.win  = win
    self.lose = lose
    self.done = False