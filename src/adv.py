from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("PLayer1", room["outside"])
print(player.currentRoom)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    cmd = input("Please input n/s/e/w: ").split(" ")
    if cmd[0] == "q":
        print("Thank you for playing!")
        break
    elif cmd[0] in ("n", "s", "e", "w") and len(cmd) == 1:
        player.travel(cmd[0])
    elif cmd[0] == "add" and len(cmd) > 2:
        item = cmd[1]
        desc = cmd[2]
        player.currentRoom.addItemToRoom(item, desc)
    elif cmd[0] in ("take", "get") and len(cmd) > 1:
        item = cmd[1]
        player.addItemToPlayer(item)
    elif cmd[0] in ("drop", "remove") and len(cmd) > 1:
        item = cmd[1]
        player.dropItemFromPlayer(item)
    elif cmd[0] in ("i", "inventory") and len(cmd) == 1:
        print(f"\nInventory: {[item.name for item in player.items]}\n")
    else:
        print("\nInvalid, please try again.\n")