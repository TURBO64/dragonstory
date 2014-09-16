import textwrap
import colorama

class Console:
  def __init__(self):
    # enable win32 color compatibility
    colorama.init()

    # -- color escape codes
    self.grey   = '\033[0;37m' # grey
    self.white  = '\033[1;37m' # white
    self.black  = '\033[1;30m' # black
    self.red    = '\033[1;31m' # red
    self.green  = '\033[1;32m' # green
    self.yellow = '\033[1;33m' # yellow
    self.blue   = '\033[1;34m' # blue
    self.purple = '\033[1;35m' # purple
    self.cyan   = '\033[1;36m' # cyan
    self.reset  = '\033[0m'    # reset
    # -- end of colors

    # init parser
    self.verb, self.subj = None, None

  # parse user input
  def parser(self):
    self.say()
    cmd = input("> ").lower()
    if cmd:
      words = cmd.split()
      self.verb = words[0]  # first word in list
      self.subj = words[-1] # last word

  # print a formatted string
  def say(self, newmsg=None, color=None):    
    if newmsg:
      fmsg = textwrap.dedent(textwrap.fill(newmsg))
      if color != None:
        print(color + fmsg + self.reset)
      else:
        print(fmsg)
    else:
      print()

  # describe a room and list items (if any)
  def describe(self, target):
    self.say(target.name, self.white)
    self.say(target.descr)
    if target.items:
      self.say()
      if len(target.items) > 1:
        self.say("Things that are here: ")
        for item in target.items:
          self.say("a " + item.name)
      else:
        for item in target.items:
          self.say("There is a " + item.name + " here.")

  # play event
  def play(self, target):
    self.say("")
    self.say(target.descr)