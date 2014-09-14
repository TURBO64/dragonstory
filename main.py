#!/usr/bin/python3
# dragon story
# a text adventure game where you play as a dragon

from player import *
from item import *
from event import *
from room import *
from console import *

# init player
player = Player()

# -- init items --
item_key = Item("key", True,
"A small, black metal key with a twisted shape. When you hold it "
"up to the light at the right angle, it seems to give off a dark, "
"blood-red glow.")
item_sword = Item("sword", True,
"A common weapon carried by human adventurers. "
"You have no need for weapons, and the blade is dull and chipped. "
"It could be useful for something else, though.")
# -- end items --

# -- init events --
event_roar = Event("newroom", None,
  "You hear a distant roar...")
event_earthquake = Event("takeitem", None,
  "You feel the ground shake beneath your feet.")
event_bridgedeath = Event("useitem", "death",
  "The rickety old bridge was never built to support the "
  "weight of a dragon. The ropes snap and you plummet into "
  "the chasm to your death.")
# -- end events --

# -- init rooms --
room0 = Room(
  "Lair", 1, 4, [item_key], [event_earthquake],
  "You are in a dark, filthy cave. There are charred bones and "
  "bits of rusted weaponry scattered all over the floor. At the north "
  "end of the cave is a large, open crevice in the rock wall.")
room1 = Room(
  "Tunnel", 1, 3, None, None,
  "The long winding tunnel is also littered with the remains of "
  "the human invaders. To the west you can see daylight from outside "
  "the cavern. To the south is the entrance to your lair.")
room2 = Room(
  "Cliff", 0, 3, None, [event_roar],
  "You are now standing at the opening of the cave, on the side of a "
  "cliff. There is a rickety old rope bridge here that leads to the "
  "north. It looks rather flimsy and dangerous.")
room3 = Room(
  "The Bridge Of Death", 0, 2, None, [event_bridgedeath],
  "You decide to try and cross the bridge. Before you even get halfway "
  "across, you hear a loud cracking sound under your feet.")
room4 = Room(
  "Mountains", 0, 1, [item_sword], None,
  "The steep terrain here makes it difficult to walk. To the south is "
  "the rickety rope bridge. A worn path leads down the mountains into a "
  "forest to the north.")
room5 = Room(
  "Forest Entrance", 0, 0, None, [event_roar],
  "You're now standing near a thick forest of evergreen trees. The dirt "
  "path goes east through the woods. To the south you can see the snowy "
  "mountains where your lair is." )
room6 = Room(
  "Placeholder", 1, 0, None, None,
  "Filler text" )
room7 = Room(
  "Placeholder", 2, 0, None, None,
  "Filler text" )
room8 = Room(
  "Placeholder", 2, 1, None, None,
  "Filler text" )
room9 = Room(
  "Placeholder", 2, 2, None, None,
  "Filler text" )
roomA = Room(
  "Placeholder", 3, 2, None, None,
  "Filler text" )
roomB = Room(
  "Placeholder", 4, 2, None, None,
  "Filler text" )
roomC = Room(
  "Placeholder", 4, 1, None, None,
  "Filler text" )
roomD = Room(
  "Placeholder", 4, 0, None, None,
  "Filler text" )
roomE = Room(
  "Placeholder", 4, 3, None, None,
  "Filler text" )
roomF = Room(
  "Placeholder", 4, 4, None, None,
  "Filler text" )
# -- end rooms --

# -- init world --
world = [
  [room5, room6, room7,  None, roomD ],
  [room4,  None, room8,  None, roomC ],
  [room3,  None, room9, roomA, roomB ],
  [room2, room1,  None,  None, roomE ],
  [ None, room0,  None,  None, roomF ]]
# -- end world

# set player location
player.room = world[player.y][player.x]

# init console
cons = Console()

# start the game
cons.say("Dragon Story v1.0 by zb", cons.yellow)
cons.say("")

# describe room
cons.describe(player.room)

# -- begin main loop --
while player.dead == False:
  # flag current room as visited
  player.room.flag = True
  
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
      if event.flag == False:

        # -- room triggers --
        if event.trigger == "random":      # when a 7 is rolled
          if random.randrange(12) == 7:
            cons.play(event)

        if event.trigger == "oldroom":     # every time player enters room
          cons.play(event)

        if event.trigger == "newroom":     # first player enters room
          cons.play(event)
          event.flag = True

        if event.trigger == "takeitem":    # player takes an item
          if player.items:
            if player.items[0].taken == True:
              cons.play(event)
              event.flag = True
        # -- end of room triggers --
        # -- room outcomes --
        if event.outcome == "death":       # game over, man
          cons.play(event)
          player.dead = True

  # handle input (if player is alive)
  if player.dead == False:
    cmd = input("> ").lower()
    cons.parse(cmd)

    # -- begin command list --

    if cons.verb in ["look", "l", "examine", "exa"]:
      if cons.subj != cons.verb:
        for item in player.room.items:
          if cons.subj in item.name:
            cons.describe(item)
      else:
        cons.describe(player.room)
    elif cons.verb in ["inv", "inventory"]:
      cons.say("You are carrying: ")
      if player.items:
        for item in player.items:
          cons.say(item.name)
      else:
        cons.say("Nothing.") 
    elif cons.subj in ["north", "n"]:
      player.dx, player.dy = 0, -1
    elif cons.subj in ["south", "s"]:
      player.dx, player.dy = 0, 1
    elif cons.subj in ["west", "w"]:
      player.dx, player.dy = -1, 0
    elif cons.subj in ["east", "e"]:
      player.dx, player.dy = 1, 0
    elif cons.verb in ["fly", "jump"]:
      if player.room is room2:
        cons.say("You fly across the chasm...")
        cons.say("")
        player.dy = -2
      elif player.room is room4:
        cons.say("You fly across the chasm...")
        cons.say("")
        player.dy = 2
      else:
        cons.say("There's no reason to do that now.")
    elif cons.verb in ["quit", "q", "exit"]:
      player.dead = True
    elif cons.verb in ["help", "h", "?"]:
      cons.say("Commands:")
      cons.say("(n)orth, (s)outh, (w)est, (e)ast - move around")
      cons.say("(l)ook - examine things")
      cons.say("(q)uit - quit the game")
      cons.say("(h)elp - display this list")
    elif cons.verb in ["pos", "position"]:
      cons.say(str(player.x) + ", " + str(player.y) )
    else:
      cons.say("I don't understand that.")
    # -- end command list --

# -- end main loop --

cons.say("Thanks for playing!")

# keep window open for ide
input("\r\nPress any key to continue")