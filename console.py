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

  # parse user input
  def parse(self, string):
    words = string.split()
    self.verb = words[0]  # what to do
    self.subj = words[-1] # what to do it on

  # print a formatted string
  def say(self, newmsg, color=None):    
    fmsg = textwrap.dedent(textwrap.fill(newmsg))
    if color != None:
      print(color + fmsg + self.reset)
    else:
      print(fmsg)

  # describe something
  def describe(self, target):
    self.say(target.name, self.white)
    self.say(target.descr)
    self.say("")
    if target.items:
      for x in target.items:
        self.say("There is a " + x.name + " here.")
        self.say("")

  # play event
  def play(self, target):
    self.say(target.descr)
    self.say("")