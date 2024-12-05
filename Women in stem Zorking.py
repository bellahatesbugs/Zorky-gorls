
class Room:
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.exits = exits if exits else {}

    def describe(self):
        print(f"\nYou are in {self.name}. {self.description}")
        if self.items:
            print("You see the items: " + ", ".join(self.items))
        if self.exits:
            print("Exists: " + ", ".join(self.exits.keys()))

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

class Game:
    def __init__(self):
        # Define rooms
        self.start_room = Room(
            name="",
            description="",
            items=[""],
            exits={""}
        )
        self.hallway = Room(
            name="",
            description="",
            items=[""],
            exits={""}
        )
        self.treasure_room = Room(
            name="",
            description="",
            items=[""],
            exits={""}
        )

        # Link rooms
        self.rooms = {
            "": self.start_room,
            "": self.hallway,
            "": self.treasure_room
        }

        # Current state
        self.current_room = self.start_room
        self.inventory = []

    def print_inventory(self):
        if self.inventory:
            print("Inventory includes: " + ", ".join(self.inventory))
        else:
            print("You Have no items in your inventory")

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room_name = self.current_room.exits[direction]
            self.current_room = self.rooms[next_room_name]
            self.current_room.discribe()
        else:
            print("That is not an option stupid!!")

    def take_item(self, item):
        if item in self.current_room.items:
            self.current_room.remove_item(item)
            self.inventory.append(item)
            print(f"You picked up {item}")
        else:
            print(f"There's no {item} here??? what are you thinking")

    def drop_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
            print(f"You dropped the {item}.")
        else:
            print(f"You don't have that item dummy")

    def main_menu(self):
        while True:
            print("\nGame Start Menu")
            print("Select one of the following:")
            print("1 - Play the Game")
            print("2 - Instructions")
            print("3 - Load Score")
            print("4 - Quit")
            choice = input("Enter your choice: ")
            self.current_room.describe()

            if choice == "1":
                print("You are PLAYING THE GAME.")
                # Call 'Play Game' function here

            elif choice == "4":
                print("You are READING THE INSTRUCTIONS.")
                # Call 'Instructions' function here
            elif choice == "5":
                print("You are LOADING THE SCORE.")
                # Call 'Game Settings' function here
            elif choice == "6":
                print("You are ENDING THE GAME.")
                break
            else:
                print("You made an Illegal Choice.")

if __name__ == "__main__":
    game = Game()
    game.start()

