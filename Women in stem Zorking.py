
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
            name="Main Cavern",
            description="You are in a large, circular cavern. There are three tunnels to the northwest, northeast, and south. It is dark. There is a rusted metal chest against the wall. There are tunnels branching off on the North West, North East, and South sides.",
            items=["Flashlight", "Batteries"],
            exits={"Northwest Tunnel", "Northeast Tunnel"}
        )
        self.NorthwestTunnel = Room(
            name="Northwest Tunnel",
            description="At the end of the tunnel, laying on the ground, is a glittering sword of silver metal. It has dried blood on the tip. There is only one way out, the way you came.",
            items=["Sword"],
            exits={"Main Cavern"}
        )
        self.NortheastTunnel = Room(
            name="Northeast Tunnel",
            description="You enter the tunnel and hear a loud roar. There is a large green troll at the other end of the tunnel, and it definitely heard you coming.",
            exits={"Main Cavern"}
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

    def f_one_ne_monster():
    monster_name = "Troll"
    monster_health = 30
    player_health = 20
    print(
        "You enter the tunnel and hear a loud roar. There is a large green troll at the other end of the tunnel, and it definitely heard you coming.")
    print("The Troll holds a club in one hand, which would definitely hurt to get hit by.")
    print("The Troll is large, but slow. Quick attacks would best the monster.")

    def attack():
        player_health = 20
        monster_health = 30
        monster_name = "Troll"
        while player_health > 0 and monster_health > 0:
            turn = 1
            if turn == 1:
                weapon = input("What would you like to attack with?: ")
                print(f"You attack the {monster_name} with your {weapon}")
                if weapon == 'sword' or 'bow':
                    damage = 10
                    monster_health -= damage
                    turn = 2
                elif weapon == 'knife':
                    damage = 20
                    monster_health -= damage
                    turn = 2
            elif turn == 2:
                damage2 = random.randint(1, 5)
                player_health -= damage2
                print(f"The {monster_name} attacks you.")
                print(f"You take {damage2} damage. You have {player_health} health left.\n")

        if player_health <= 0:
            print(f"You have been defeated by the {monster_name}.")
            main_cavern()
        if monster_health <= 0:
            print(f"The {monster_name} has died.")

    def defend():
        monster_name = "Troll"
        player_health = 20
        if random.randint(1, 2) == 1:
            print(f"You avoid the trolls attack. Your health remains at {player_health}.")
        else:
            damage = random.randint(1, 5)
            player_health -= damage
            print(f"The {monster_name} attacks you.")
            print(f"You take {damage} damage. You have {player_health} health left.\n")

    def flee():
        print("You flee back into the large cavern.")
        main_cavern()

    while monster_health > 0 and player_health > 0:
        print(f"The {monster_name} has {monster_health} health.")
        print(f"You have {player_health} health.")
        action = input("What would you like to do? (attack, defend, flee)")
        if action == 'attack':
            attack()
        elif action == 'defend':
            defend()
        elif action == 'flee':
            flee()
        else:
            input("Please choose to attack, defend, or flee.")


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

