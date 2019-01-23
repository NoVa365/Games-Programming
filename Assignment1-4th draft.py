# This variable sets up the core game loop, this line states that the player is not dead at the start of the game.

dead = False
knife = False
crowbar = False

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
#This is a function that play safter the player makes the decision to send someone else up stairs instead of going alone.
def someoneelse():
    print("About 30 miniutes have past and you haven't heard anything from the officer you sent upstairs, you decide"
          " to head up there yourself to see what's going on\n You hear a loud bang coming from the attic, as you go"
          " to open the hatch to the attic it blows open and something lunges at you killing you")
    return True

#This function will allow the player to navigate the kitchen part of the house, there are optional items here.
def kitchen():
    print("You enter the kitchen, everything around is somewhat run down and old.")
    kitchen1 = input("You don't immediately see anything that looks out of the ordinary you decide that taking"
                     " a closer look could be useful")
    if kitchen1 in ("check worktops", "Look at worktops","worktops"):
        print("Looking at the worktops they are full of dust and decay, you do notice that on the left hand side there"
              " is a crowbar you take this with you")
        inventory.append("Crowbar")
        global crowbar
        crowbar = True
    if kitchen1 in ("check fridge", "Look in fridge", "fridge"):
        print("You open the fridge and notice a horrible smell coming from decaying food, there is nothing of interest"
              " inside.")
    if kitchen1 in ("Look around"):
        print("You can see a fridge and some cupboards that might be worth looking into, the rest of the room looks empty")
    #if kitchen1 in ("Go back", "Back", "Go back to hall"):
    #Here will be a line of code going back to the hall way.
    else:
        print("I'm not sure what you mean, try typing again")











#   This line of code defines the players inventory at the start of the game and can be added to later on.


inventory = ["Lighter", "cigerettes", "phone", "journal", "Handgun"]


#   The start of the actual game, everything before this was functions and defining variables.

#Starts the loop for the game here.
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

#The player chooses to pick up the knife here, at the moment there is no use for it in the code later on.
    part2 = input("You find it odd as these two holes are the only injuries on the victims body and yet the victim has " 
                  "completely bled out over the floor\nSomething like this would normally be impossible for "
                  "such a small wound.\n By the floor next to the body is a knife would you like to pick it up?")
    if part2.lower() == "yes":
        inventory.append("knife")
        knife = True
        print("You add the knife to your inventory: current inventory" , inventory)
    elif part2.lower() == "no":
        print("You decided it's better to not obstruct evidence in a crime scene and leave the knife where it is")
    else:
        print("I'm not sure what you mean try typing again")

    print("After an hour at the crime scene the police officers have started to get lazy and are beginning to lose"
          " focus\n All of a sudden you hear a loud thump upstairs.")

#This decision leads to the players death if they decide to send someone else upstairs.
    part3 = input("Do you wish to go upstairs yourself or send someone else upstairs in your stead?")
    if part3.lower() in ("alone", "by myself"):
        print("You decide to investigate the sound yourself")
        dead = yourself()

    elif part3.lower() in ("someone else", "another"):
        print("You decide it's best to send one of the other police officers to investigate the noise"
              " as you are still looking around")
        dead = someoneelse()
        break
    else:
        print("I'm not sure what you mean try typing again")

#The wrong decision here for the player results in death.
    part4 = input("After surviving the monsters attack you notice that the monsters body disapears into dust\n"
                  "Do you want to inspect the ash? ")
    if part4.lower() in ("yes", "ye", "y"):
        print("You notice that the clothes that monster was wearing are still on the floor where the monster laid,"
              " covered in the ash\n Upon closer inspection you see that there is a small piece of paper"
              " with the number 176 str on it. It's worth a look to find out what's going on.")
    elif part4.lower() in ("no", "n"):
        print("You decided it's better to not go routing around something,"
              " all of this is weird enough without having to touch some unknown substance\n"
              " However the dust disintegrates the floor you are standing on and you fall through the floor to your"
              " death")
        break
#Next chapter will focus on traversing a house and using found objects in order to get through it.
    print("Chapter 2")
    print("You pull up outside the house you found the address for on the monster.\n"
          " You leave your vehicle and step out to see an old house looking decrepit in look and feel.  ")
    part5 = input("You see a heavy door at the front of the house and a small hatch to the side which way do you want"
                  " to get in?")
    if part5.lower() in ("door", "go to door", "knock on door", "Open door" ):
        print("The door seems to be locked and there is no answer instead you try the hatch and it opens, you take the"
              " stairs leading down")

    elif part5.lower() in ("go to hatch", "hatch"):
        print("You notice the hatch is open and make your way down a small staircase under the house")

    part6 = input("At the base of the stairs you find yourself inside some kind of basement.\n You see a door way"
                  " in front of you and a staircase leading up")
    if part6.lower() in ("go to room", "room", "look at room", "investigate room"):
        print("You walk into the small room however there is nothing of interest apart from a few strange markings"
              " on the walls however you do not understand what these mean.")
    elif part6.lower() in ("stairs", "go to stairs", "go up stairs" "staircase"):
        print("You head up the stairs and find yourself in the main hall of the house.\n you can see the kitchen,"
              " a living room and stairs going up")

    part7 = input("The house is quiet so you decide you should look around")
    if part7.lower() in ("kitchen", "go to kitchen", "investigate kitchen"):
        print("You decide to go look around the kitchen")
        dead = kitchen()











