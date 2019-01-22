# This variable sets up the core game loop, this line states that the player is not dead at the start of the game.

dead = False

# This whole part is a function that plays out when a certain decision is made later on in the game.


def yourself():
    print("You draw your handgun and slowly traverse your way up the stairs\nYou hear the sound again it is still above"
          " you\nIt seems to be coming from the attic")
    decision1 = input("There is a small hatch which can be used to access the attic do you want to enter?")
    if decision1 in ("yes"):
        print("The room is extremely dark however you can hear a small squelching sound on the other side of the room")
    elif decision1.lower() in "no":
        print("You do not enter the attic and something comes crashing down through the ceiling"
              " and kills you where you stand")
        return True

# Carrying on the initial function, however with more routes for the player to go down.
    decision2 = input("You remember you have a lighter with you do you wish to use it to light up the room?").lower()
    if decision2 == "yes":
        print("Using the lighter has helped somewhat and you can see a little but infront of you\nYou see a dark"
              " figure in the corner of the room hunched over")

    decision3 = input("do you wish to call out to the figure or approach")
    if decision3 == "approach":
        print("The figure turns around to reveal a monsterous face and huge claws and teeth it lunges"
              " at you before you can react and you are killed")
        # global dead
        return True
    elif decision3 == "call out":
        print("You call out the figure and you see it slowly stands up and turns to you revealing a monsterous face"
              " and huge claws and teeth the monster lunges at you and you shoot it down and kill it.")
        return False


#def part4yes():
    #print("The piece of paper that you found must be a good clue as to finding out what happened here and what's going on overall, because of this you should try to solve what the message means.")
    #decision4 = input("")

#   This line of code defines the players inventory at the start of the game and can be added to later on.


inventory = ["Lighter", "cigerettes", "phone", "journal", "Handgun"]


#   The start of the actual game, everything before this was functions and defining variables.


while not dead:
    print("You are Tony Rogers an ace detective who's been on some of the most dangerous cases in the world\nYou"
          " are on your way to a new crime scene where you have been called by the local police.\n")

#   This part starts the first decision for the player, a while loop is needed here as the player has to inspect
#   the correct part of the body in order to proceed.
    while True:
        part1 = input("As you walk into the crime scene you notice the body laying in a pool of blood which body part"
                      " do you wish to inspect?\n head\n body\n arms\n legs\n")
        if part1.lower() == "arms":
            print("After inspecting the arms you find two small holes at the victims wrists\n.")
            break
        elif part1.lower() in ("head", "body", "legs"):
            print("You inspect the body part and find nothing out of the ordinary maybe you should try somewhere else")
        else:
            print("There is no such body part.")

    part2 = input("You find it odd as these two holes are the only injuries on the victims body and yet the victim has " 
                  "completely bled out over the floor\nSomething like this would normally be impossible for "
                  "such a small wound.\n By the floor next to the body is a knife would you like to pick it up?")
    if part2.lower() == "yes":
        inventory.append ("knife")
        print("You add the knife to your inventory: current inventory" , inventory)
    elif part2.lower() == "no":
        print("You decided it's better to not obstruct evidence in a crime scene and leave the knife where it is")

    print("After an hour at the crime scene the police officers have started to get lazy and are beginning to lose"
          " focus\n All of a sudden you hear a loud thump upstairs.")

    part3 = input("Do you wish to go upstairs yourself or send someone else upstairs in your stead?")
    if part3.lower() in ("alone", "by myself"):
        print("You decide to investigate the sound yourself")
        dead = yourself()

    elif part3.lower() in ("someone else" , "another"):
        print("You decide it's best to send one of the other police officers to investigate the noise"
              " as you are still looking around")

    part4 = input("After surviving the monsters attack you notice that the monsters body disapears into dust\n"
                  "Do you want to inspect the ash? ")
    if part4.lower() in ("Yes", "ye", "y"):
        print("You notice that the clothes that monster was wearing are still on the floor where the monster laid,"
              " covered in the ash\n Upon closer inspection you see that there is a small piece of paper"
              " with the number 176 str on it. ")
    elif part4.lower() in ("no", "n"):
        print("You decided it's better to not go routing around something,"
              " all of this is weird enough without having to touch some unknown substance")

    print("Chapter 2")




