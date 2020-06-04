# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def travel(self, direction):
        nextRoom = self.currentRoom.getNextRoomDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("\nYou can't move that way.\n")

    def addItemToPlayer(self, inputItem):
        roomItems = self.currentRoom.items
        for item in roomItems:
            if item.name == inputItem:
                self.items.append(item)
                roomItems.remove(item)
                item.on_take()
                return None
        print(f"\n{inputItem} is not in {self.currentRoom.name}\n")

    def dropItemFromPlayer(self, inputItem):
        roomItems = self.currentRoom.items
        for item in self.items:
            if item.name == inputItem:
                self.items.remove(item)
                roomItems.append(item)
                item.on_drop()
                return None
        print(f"\n{inputItem} is not in {self.name}'s inventory\n")