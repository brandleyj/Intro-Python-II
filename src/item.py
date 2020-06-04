class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self):
        print(f"\nYou have picked up {self.name}\n")

    def on_drop(self):
        print(f"\nYou have dropped {self.name}\n")