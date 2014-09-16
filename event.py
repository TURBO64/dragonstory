class Event:
  def __init__(self, trigger, outcome, solution, interactive, descr, win, lose):
    self.trigger = trigger
    self.outcome = outcome
    self.solution = solution
    self.interactive = interactive
    self.descr = descr
    self.win  = win
    self.lose = lose
    self.done = False