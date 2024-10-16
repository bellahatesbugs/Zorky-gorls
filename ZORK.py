import math
import random
from sys import float_repr_style

def random_bool():
    return random.choice(True,False)
inventory = []

player_health = 20

def instructions(): #this defines instructions
    print("\n----Instructions\n")
    print("In this game, you are exploring a cave and trying to defeat monsters to escape.")
    print("There are helpful items scattered throughout the cave.")
    print("Good luck adventurer!")

def settings(): #this defines settings, and calls the menu
    print("\n----Settings----\n")
    start_menu()

def play_game(): #this will be for playing the game
    print("\n----Play Game----\n")
    game_menu()

def quit_game(): #this defines the quit game command
    print("\n----Quit Game----\n")
    print("Thank you for playing!")
    print("We hope to see you next time!")

def start_menu(): #this is the menu that can be used to call all the functions listed below
    print("\n----Menu----\n")
    print("1. Instructions")
    print("2. Play Game")
    print("3. Settings")
    print("4. Quit Game")

    choice = int(input("What would you like to do: "))

    if choice == '1':
        instructions() #calls instructions function
        start_menu() #calls menu after the instructions run
    elif choice == '2':
        play_game() #calls play_game function
        start_menu() #calls menu after the play_game runs
    elif choice == '3':
        settings()
    elif choice == '4':
        quit_game() #calls quit_game function
        exit() #exits the game
    else:
        print("Invalid answer. Select 1, 2, 3, or 4.") #this runs if the player doesn't select one of the options
        start_menu() #recalls the menu

def main_cavern():
    print("You are in a large, circular cavern. There are three tunnels to the northwest, northeast, and south."
          "It is dark. There is a rusted metal chest against the wall. "
          "There are tunnels branching off on the North West, North East, and South sides.")
    flashlight_before()
    draw_circle(6)
    def main_cavern_menu():
        chest = input("Would you like to open the chest?")
        if chest:
            batteries()
            flashlight_after()
        else:
            print("You choose to not open the chest.")
        first_floor_movement = input("Where would you like to go? ").strip().lower()
        if first_floor_movement == 'northwest' or 'nw':
            nw_fone()
        elif first_floor_movement == 'northeast' or 'ne':
            ne_fone()
        elif first_floor_movement == 'south' or 's':
            s_fone()
        else:
            print("You cannot go that way.")
            first_floor_movement = input("Where would you like to go? ").strip().lower()
    main_cavern_menu()


# noinspection SpellCheckingInspection
def nw_fone():
    print("At the end of the tunnel, laying on the ground, is a glittering sword of silver metal."
          "It has dried blood on the tip. There is only one way out, the way you came.")
    draw_rectangle()
    def nw_fone_menu():
        sword_choice = input("Would you like to pick up the sword? ")
        if sword_choice:
            sword()

        else:
            print("You chose not to pick up the sword.")

# noinspection SpellCheckingInspection
def ne_fone():
    print("You enter the tunnel and hear a loud roar. There is a large green troll at the other end of the tunnel,"
          "and it definitely heard you coming.")
    draw_rectangle()
    def ne_fone_menu():
        f_one_ne_monster()
    ne_fone_menu()


# noinspection SpellCheckingInspection
def s_fone():
    print("You walk through the tunnel to find nothing but stalactites and loose gravel.")
    draw_rectangle()
#do input movement

def nw_ftwo():
    print("You enter the tunnel and see a yellow troll facing away from you at the end of the tunnel."
    "Its foul smell strings your nostrils.")
    draw_rectangle()


def ne_ftwo():
    print("You almost trip over a medium-sized hunting knife as you enter the northeast tunnel."
          "The rest of the tunnel is empty.")
    draw_rectangle()
    def ne_ftwo_menu():
        knife_choice = input("Would you like to grab the knife? (yes or no): ")
        if knife_choice:
            knife()
        else:
            print("You chose not to pick up the knife.")


# noinspection SpellCheckingInspection
def ne_fthree():
    print("You see a towering blue figure immediately when you enter the tunnel. "
    "Its mouth drips with saliva when it spots you. You can barely see a rope ladder behind the tall troll.")
    draw_rectangle()
    #def ne_fthree_menu():

# noinspection SpellCheckingInspection
def se_fthree():
    print("Two smaller blue trolls sleep peacefully piled on top of eachother in the corner. "
          "The one on top’s ear perks up at the sound of you entering the tunnel.")
    draw_rectangle()
    #def se_fthree_menu():

# noinspection SpellCheckingInspection
def se_ffour():
    print("Upon entering the southeast tunnel, you see there is a strong, long rope coiled up on the floor.")
    draw_rectangle()
    #def se_ffour_menu():

# noinspection SpellCheckingInspection
def sw_ffour():
    print("You hear a growl as you enter the southwest tunnel, "
          "and see a large purple troll guarding a beat-up rope ladder.")
    draw_rectangle()
    #def sw_ffour_menu():

# noinspection SpellCheckingInspection
def sw_ffive():
    print("As you enter the southwest tunnel, you notice a bow hung up on one of the walls. "
          "You also notice a quiver of arrows leaning up against the wall.")
    draw_rectangle()
    #def sw_ffive_menu():

# noinspection SpellCheckingInspection
def nw_ffive():
    print("A guttural roar hits your ears as you enter the northwest tunnel, and your body fills with shock. "
          "There is a humongous blood-red troll staring directly at you, holding a spiked club")
    draw_rectangle()
    #def nw_ffive_menu():


def forest():
    print("You climb up the rope ladder and bright sunlight stings your eyes. "
          "You look around to find tall trees in all directions.")
    draw_square()
    #def forest_menu():

def bedroom():
    print("When you try to move, your body freezes, and you see the world around you going dark. "
          "You wake up, and you’re in a soft bed. Your bed. "
          "You look around. It’s your childhood bedroom.")
    draw_square()
    #def bedroom_menu():

def game_menu():
    if main_cavern():
        main_cavern()
    elif nw_fone():
        nw_fone()
    elif ne_fone():
        ne_fone()
    elif s_fone():
        s_fone()
    elif nw_ftwo():
        nw_ftwo()
    elif ne_ftwo():
        ne_ftwo()
    elif ne_fthree():
        ne_fthree()
    elif se_fthree():
        se_fthree()
    elif se_ffour():
        se_ffour()
    elif sw_ffour():
        sw_ffour()
    elif sw_ffive():
        sw_ffive()
    elif nw_ffive():
        nw_ffive()
    elif forest():
        forest()
    elif bedroom():
        bedroom()


def draw_circle(radius):
    # dist represents distance to the center
    # for horizontal movement
    for i in range((2 * radius) + 1):
        for j in range((2 * radius) + 1):
            dist = math.sqrt((i - radius) * (i - radius) +
                             (j - radius) * (j - radius))
            # dist should be in the
            # range (radius - 0.5)
            # and (radius + 0.5) to print stars(*)
            if radius - .5 < dist < radius + 0.5:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def draw_rectangle():
    # First For Loop (1-10)
    for a in range(1, 11):  # Loop from 1 to 10 (inclusive)
        print("*", end="")  # Print an asterisk (*) without a newline
    print()  # Move to the next line after printing 10 asterisks
    # Second For Loop (1-5)
    for b in range(1, 6):  # Loop from 1 to 5 (inclusive)
        # Inner For Loop (1 time)
        for c in range(1, 2):  # Loop once
            print("*", end="")  # Print an asterisk (*) without a newline
        # Inner For Loop (8 times)
        for d in range(1, 9):  # Loop from 1 to 8 (inclusive)
            print(" ", end="")  # Print a space ( ) without a newline
        print("*")  # Print an asterisk (*) and move to the next line
    # Third For Loop (1-10)
    for e in range(1, 11):  # Loop from 1 to 10 (inclusive)
        print("*", end="")  # Print an asterisk (*) without a newline
    print()
def draw_square():
    # First For Loop (1-10)
    for a in range(1, 11):  # Loop from 1 to 10 (inclusive)
        print("*", end="")  # Print an asterisk (*) without a newline
    print()  # Move to the next line after printing 10 asterisks

    # Second For Loop (1-5)
    for b in range(1, 4):  # Loop from 1 to 5 (inclusive)
        # Inner For Loop (1 time)
        for c in range(1, 2):  # Loop once
            print("*", end="")  # Print an asterisk (*) without a newline

        # Inner For Loop (8 times)
        for d in range(1, 9):  # Loop from 1 to 8 (inclusive)
            print(" ", end="")  # Print a space ( ) without a newline

        print("*")  # Print an asterisk (*) and move to the next line

    # Third For Loop (1-10)
    for e in range(1, 11):  # Loop from 1 to 10 (inclusive)
        print("*", end="")  # Print an asterisk (*) without a newline
    print()
start_menu()

def flashlight_before():
    print("You look around the large cavern and check your pockets. "
          "You find a large black flashlight that won’t turn on.")
    inventory.append("Flashlight")

def flashlight_after():
    print("Clicking the flashlight on this time illuminated the cave with a bright beam of light. "
          "The dark tunnels didn’t feel so dark anymore")

def batteries():
    print("Within the chest lay two large batteries, which fit perfectly into the flashlight.")

def sword():
    print("At the end of the tunnel, laying on the ground, is a glittering sword of silver metal. "
          "It has dried blood on the tip.")
    inventory.append("Sword")

def f_one_ne_monster():
    monster_name = "Troll"
    monster_health = 30
    player_health = 20
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
                damage2 = random.randint(1,5)
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
        if random.randint(1,2) == 1:
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

#A minimum of five Room Functions with the following nested functions:
# Room Menu Function
# Room Description Function
# Room Map/Floor Plan Function
# A minimum of three Item Functions
# A minimum of one Monster Function
# A coded Player/Monster Fight Sequence

