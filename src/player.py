# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.currentRoom = room

    def travel(self, direction):
        nextRoom = self.currentRoom.getNextRoomDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("\nYou can't move that way.\n")
