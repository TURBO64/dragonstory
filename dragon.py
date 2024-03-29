#!/usr/bin/python3
# Dragon Story by zb
# A fantasy text adventure game where YOU are the dragon!

import os
import platform

from console import *
from player import *
from item import *
from event import *
from room import *

newgame = True

# ---- begin restart loop ----
while newgame:

  # init console and player
  cons = Console()
  player = Player()

  # ---- init all items ----
  item_skull = Item("human skull", True,
  "An old human skull, cracked and dried out.")

  item_sign = Item("sign", False,
  "It reads: DANGER! BEWARE OF DRAGON")

  item_mushroom = Item("strange mushroom", True,
  "A strange red mushroom covered in white spots.")

  item_ashes = Item("ashes", True,
  "The burnt remains of the forest troll.")

  item_shield = Item("shield", True,
  "A large wooden tower shield.")

  item_key = Item("silver key", True,
  "A small, silver key")
  # ---- end of items ----

  # ---- init all events ----
  event_earthquake = Event(
    "newroom", None, None, False,
    "You feel the ground shake beneath your feet for a moment...",
    None, None
  )
  event_growl = Event(
    "newroom", None, None, False,
    "You hear a distant growling sound...",
    None, None
  )
  event_bridge = Event(
    "room", "death", None, False,
    "The rickety old bridge was never built to support the "
    "weight of a dragon. The ropes snap and you plummet into "
    "the chasm to your death.",
    None, None
  )
  event_mushroom = Event(
    "room", "death", None, False,
    "You eat the strange mushroom. Whoops! That mushroom was "
    "extremely poisonous! You begin to hallucinate and feel very "
    "sick to your stomach. After a while, you succumb to the deadly "
    "poison. Didn't anyone tell you not to eat wild mushrooms?",
    None, None
  )
  event_troll = Event(
    "newroom", None, ["fire", "breathe"], True,
    "As you near the bridge, you are ambushed by a huge, hairy troll. "
    "Its lips curl back revealing its large blood-stained fangs. Suddenly, "
    "it lets out a horrible roar and starts charging straight at you!",
    # if the player wins
    "With all your might, you breathe forth a large plume of fire and engulf "
    "the forest troll in flames. The beast thrashes about wildly for a moment "
    "and then jumps into the river and swims away. Well done!",
    # if the player loses
    "The forest troll isn't messing around. The giant monster gives you a "
    "thorough and brutal trouncing and then devours your body whole."
  )
  # ---- end of events ----

  # ---- init all rooms ----
  room0 = Room(
    "Lair", 1, 4, [], [],
    "You are in a dark, filthy cave. There are charred bones and "
    "bits of rusted weaponry scattered all over the floor. At the north "
    "end of the cave is a large, open crevice in the rock wall."
   )
  room1 = Room(
    "Tunnel", 1, 3, [item_skull], [],
    "The long winding tunnel is also littered with the remains of "
    "the human invaders. To the west you can see daylight from outside "
    "the cavern. To the south is your lair."
  )
  room2 = Room(
    "Cliff", 0, 3, [], [event_earthquake],
    "You are now standing at the opening of the cave, on the edge of a "
    "steep cliff. To the west is the tunnel leading to your lair. A long "
    "rope bridge stretches to the north, across the deep chasm. It looks very "
    "flimsy and dangerous."
  )
  room3 = Room(
    "The Bridge Of Death", 0, 2, [], [event_bridge],
    "You decide to try and cross the bridge. Before you even get halfway "
    "across, you hear a loud cracking sound under your feet."
  )
  room4 = Room(
    "Mountains", 0, 1, [item_sign], [],
    "The steep terrain here makes it difficult to walk. To the south is "
    "the treacherous rope bridge. A worn path leads down the mountains into a "
    "forest to the north."
  )
  room5 = Room(
    "Forest Entrance", 0, 0, [], [event_growl],
    "You're now standing near a thick forest of evergreen trees. The dirt "
    "path goes east through the woods. To the south you can see the snowy "
    "mountains where your lair is."
  )
  room6 = Room(
    "Dark Forest", 1, 0, [item_mushroom], [],
    "The forest is very thick and overgrown here. The canopy of the trees "
    "blocks most of the sunlight and you can't see very far. To the east "
    "you can hear the sound of rushing water."
  )
  room7 = Room(
    "River", 2, 0, [], [event_troll],
    "You are standing before a stone bridge going over a river. At the end of the "
    "bridge is a dirt path leading towards a village to the south."
  )
  room8 = Room(
    "Ruined Village", 2, 1, [], [],
    "The tiny hamlet lies in ruin from your last visit and seems to be "
    "completely deserted. You see a small, partially-burned cottage to "
    "the south. To the north lies the dark forest."
  )
  room9 = Room(
    "Burned Cottage", 2, 2, [item_shield], [],
    "This is the only house that's still standing in the ruined village. "
    "An ornate coat of arms is hung on the rock wall above the ruined bed. "
    "At the other end of the room is a large wooden desk. To the east is "
    "a large chapel with a cross on the roof."
  )
  roomA = Room(
    "Chapel Entrance", 3, 2, [], [],
    "You're standing before a large chapel with stained glass windows. "
    "The front entrance is to the east. To the west is the burned cottage."
  )
  roomB = Room(
    "Placeholder", 4, 2, [], [],
    "Filler text"
  )
  roomC = Room(
    "Placeholder", 4, 1, [], [],
    "Filler text"
  )
  roomD = Room(
    "Placeholder", 4, 0, [], [],
    "Filler text"
  )
  roomE = Room(
    "Placeholder", 4, 3, [], [],
    "Filler text"
  )
  roomF = Room(
    "Placeholder", 4, 4, [], [],
    "Filler text"
  )
  # ---- end of rooms ----

  # ---- init world ----
  world = [
    [room5, room6, room7,  None, roomD ],
    [room4,  None, room8,  None, roomC ],
    [room3,  None, room9, roomA, roomB ],
    [room2, room1,  None,  None, roomE ],
    [ None, room0,  None,  None, roomF ]
  ]
  # ---- end of world ----

  # ---- game start ----

  # clear screen on windows
  if platform.system() == "Windows":
    os.system('cls')
  # clear screen on unix
  else:
    os.system('clear')
  print()

  # introduction
  cons.say("Prologue", cons.white)
  cons.say(
  "The great war is over and the land lies in ruin. You are the last "
  "of the dragons - your brethren have all been hunted down and slain by the "
  "human marauders. With their weapons and magic, they invaded and conquered "
  "your realm and the only hope left for your race is locked away in the "
  "great Wizard's Tower - the sole remaining dragon egg. Will you defeat the "
  "evil humans, recover the egg from the Wizard's Tower, and save your people "
  "from certain extinction?"
  )
  # title screen
  cons.puts(r"""
   |\                                          ,
    \\          _     _                       ||
   / \\ ,._-_  < \,  / \\  /'\\ \\/\\   _-_, =||=  /'\\ ,._-_ '\\/\\
  || ||  ||    /-|| || || || || || ||  ||_.   ||  || ||  ||    || ;
  || ||  ||   (( || || || || || || ||   ~ ||  ||  || ||  ||    ||/
   \\/   \\,   \/\\ \\_-| \\,/  \\ \\  ,-_-   \\, \\,/   \\,   |/
                     /  \                                     (
                    '----`                                     -_-
  """, cons.yellow
  )
  cons.puts(
    "                             "
    "- a text adventure game by zb", cons.brown)
  print()

  # set player location
  player.room = world[player.y][player.x]

  # describe room
  cons.describe(player.room)

  # ---- main loop ----

  while player.dead == False:
    # flag current room as visited
    player.room.visited = True
    
    # check if player moved
    if player.dx != 0 or player.dy != 0:
      # check if direction is passable
      newx = player.x + player.dx
      newy = player.y + player.dy
      if newx in range(5) and newy in range(5):
        if world[newy][newx]:
          # move player
          player.x += player.dx
          player.y += player.dy
          player.room = world[player.y][player.x]
          # auto look
          cons.describe(player.room)
        else:
          cons.say("You can't go that way.")
      else:
        cons.say("You can't go that way.")
    # reset player deltas
    player.dx, player.dy = 0, 0

    # run any room events
    if player.room.events:
      for event in player.room.events:
        if event.done == False:
          # event triggers
          if event.trigger == "newroom":     # first time player enters room
            cons.play(event)
            event.done = True
          elif event.trigger == "room":        # every time player enters room
            cons.play(event)

          # drop into the parser for interactive events
          if event.interactive:
            cons.parser()
            if cons.verb in event.solutions:
              cons.say(event.win)
              event.done = True
            else:
              cons.say(event.lose)
              event.outcome = "death"

          # event outcomes
          if event.outcome == "death":
            player.dead = True

    # handle input (if player is alive)
    if player.dead == False:

      # run the text parser
      cons.parser()

      # -- begin command list --

      # look at things
      if cons.verb in ["look", "l", "examine", "exa", "read"]:
        # check for subject
        if cons.subj != cons.verb:
          # search inventory for item
          if player.items:
            for item in player.items:
              if cons.subj in item.name:
                cons.say(item.descr)
                break
              # search room for item
              elif player.room.items:
                for item in player.room.items:
                  if cons.subj in item.name:
                    cons.say(item.descr)
                    break
                  else:
                    cons.say("You don't see a " + cons.subj + " here.")
          else:
            cons.say("You don't see a " + cons.subj + " here.")
        # describe room if no target
        else:
          cons.describe(player.room)

      # take items
      elif cons.verb in ["take", "get"]:
        if cons.subj != cons.verb:
          if player.room.items:
            for item in player.room.items:
              if cons.subj in item.name:
                if item.pickup:
                  player.items.append(item)
                  player.room.items.remove(item)
                  cons.say("Taken.")
                else:
                  cons.say("You can't pick that up.")
              else:
                cons.say("You don't see a " + cons.subj + " here.")
          else:
            cons.say("You don't see a " + cons.subj + " here.")
        else:
          cons.say("What do you want to take?")

      # drop items
      elif cons.verb in ["drop", "discard"]:
        if cons.subj != cons.verb:
          if player.items:
            for item in player.items:
              if cons.subj in item.name:
                player.items.remove(item)
                player.room.items.append(item)
                cons.say("Dropped.")
              else:
                cons.say("You're not carrying a " + item.name + ".")
          else:
            cons.say("You don't have anything to drop.")
        else:
          cons.say("What do you want to drop?")

      # list inventory
      elif cons.verb in ["inv", "inventory"]:
        cons.say("You are carrying: ")
        if player.items:
          for item in player.items:
            cons.say("a " + item.name)
        else:
          cons.say("Nothing.") 

      # move north
      elif cons.subj in ["north", "n"]:
        player.dx, player.dy = 0, -1

      # move south
      elif cons.subj in ["south", "s"]:
        player.dx, player.dy = 0, 1

      # move west
      elif cons.subj in ["west", "w"]:
        player.dx, player.dy = -1, 0

      # move east
      elif cons.subj in ["east", "e"]:
        player.dx, player.dy = 1, 0

      # fly
      elif cons.verb in ["fly", "jump"]:
        if player.room is room2:
          cons.say("You spread your wings and fly across the chasm...")
          cons.say("")
          player.dy = -2
        elif player.room is room4:
          cons.say("You fly back to the other side again...")
          cons.say("")
          player.dy = 2
        else:
          cons.say("There's no reason to do that now.")

      # breathe fire
      elif cons.subj in ["fire"]:
        cons.say("You breathe fire at nothing in particular.")

      # eat mushroom
      elif cons.verb in ["eat"]:
        if cons.subj in ["mushroom"]:
          player.room.events.append(event_mushroom)

      # quit the game
      elif cons.verb in ["quit", "q", "exit"]:
        newgame = False
        break

      # show help
      elif cons.verb in ["help", "h", "?"]:
        cons.say("Commands:")
        cons.say("(q)uit - quit the game")
        cons.say("(h)elp - display this list")
        cons.say("(n)orth, (s)outh, (w)est, (e)ast - move around")
        cons.say("(l)ook [target] - examine things (or room if no target)")
        cons.say("(inv)entory - list inventory items")
        cons.say("take [item] - pick up an item")
        cons.say("drop [item] - drop an item")
        cons.say("fly - flight")
        cons.say("fire - breathe fire")

      # print debug info
      elif cons.verb in ["debug"]:
        cons.say("Player X: " + str(player.x) )
        cons.say("Player Y: " + str(player.y) )
        cons.say("Room X: " + str(player.room.x) )
        cons.say("Room Y: " + str(player.room.y) )
        cons.say("Delta X: " + str(player.dx) )
        cons.say("Delta Y: " + str(player.dy) )
        cons.say("Parser Verb: " + cons.verb)
        cons.say("Parser Subject: " + cons.subj)

      # bad command
      else:
        cons.say("I don't understand that.")
      # ---- end command list ----

  # ---- end main loop ----

  # ask if player wants to play again
  if newgame:
    print()
    cons.say("Play again? (y or n)")
    cons.parser()
    if cons.subj in ["y", "yes"]:
      newgame = True
    else:
      newgame = False

# -- end of restart loop --

# say goodbye
cons.say("Thanks for playing!")

# keep window open on quit for IDE
input("Press any key to continue")
