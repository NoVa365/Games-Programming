# This variable sets up the core game loop, this line states that the player is not dead at the start of the game.

dead = False
knife = False
crowbar = False
key = False
bossHealth = 20
rep = 4

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
        print("You add the knife to your inventory: current inventory", inventory)
    elif part2.lower() == "no":
        print("You decided it's better to not obstruct evidence in a crime scene and leave the knife where it is")
    else:
        print("I'm not sure what you mean try typing again")

    print("After an hour at the crime scene the police officers have started to get lazy and are beginning to lose"
          " focus\n All of a sudden you hear a loud thump upstairs.")

#This decision leads to the players death if they decide to send someone else upstairs.
    while True:
        part3 = input("Do you wish to go upstairs yourself or send someone else upstairs in your stead?")
        if part3.lower() in ("alone", "by myself"):
            print("You decide to investigate the sound yourself")
            dead = yourself()
            break

        elif part3.lower() in ("someone else", "another"):
            print("You decide it's best to send one of the other police officers to investigate the noise"
                  " as you are still looking around")
            dead = someoneelse()
            break
        else:
            print("I'm not sure what you mean try typing again")

#The wrong decision here for the player results in death.
    while True:
        part4 = input("After surviving the monsters attack you notice that the monsters body disapears into dust\n"
                      "Do you want to inspect the ash? ")
        if part4.lower() in ("yes", "ye", "y"):
            print("You notice that the clothes that monster was wearing are still on the floor where the monster laid,"
                  " covered in the ash\n Upon closer inspection you see that there is a small piece of paper"
                  " with the number 176 str on it. It's worth a look to find out what's going on.")
            break
        elif part4.lower() in ("no", "n"):
            print("You decided it's better to not go routing around something,"
                  " all of this is weird enough without having to touch some unknown substance\n"
                  " However the dust disintegrates the floor you are standing on and you fall through the floor to your"
                  " death")

#Next chapter will focus on traversing a house and using found objects in order to get through it.
    print("Chapter 2")
    print("You pull up outside the house you found the address for on the monster.\n"
          " You leave your vehicle and step out to see an old house looking decrepit in look and feel.  ")
    part5 = input("You see a heavy door at the front of the house and a small hatch to the side which way do you want"
                  " to get in?")
    if part5.lower() in ("door", "go to door", "knock on door", "Open door"):
        print("The door seems to be locked and there is no answer instead you try the hatch and it opens, you take the"
              " stairs leading down")

    if part5.lower() in ("go to hatch", "hatch"):
        print("You notice the hatch is open and make your way down a small staircase under the house")

    part6 = input("At the base of the stairs you find yourself inside some kind of basement.\n You see a door way"
                  " in front of you and a staircase leading up")
    if part6.lower() in ("go to room", "room", "look at room", "investigate room"):
        print("You walk into the small room however there is nothing of interest apart from a few strange markings"
              " on the walls however you do not understand what these mean.")
    elif part6.lower() in ("stairs", "go to stairs", "go up stairs" "staircase"):
        print("You head up the stairs and find yourself in the main hall of the house.\n you can see"
              " a living room and stairs going up, you decide to check the living room first.")
    while True:
        part7 = input("You find yourself in the living room, but as you enter you hear a loud bang of the door shutting"
                " behind you, you need to find a way out")
        if part7.lower() in ("look around", "investigate"):
            print("You look around and see old furniture, some old paintings and cabinet"
                  " sitting in the corner of the room.")
        elif part7.lower() in ("check cabinet", "look in cabinet"):
            print("You look in the cabinet in a panic and find a key inside one of the draws.")
            inventory.append("Key")
            print(inventory)
        elif part7.lower() in ("open door", "door"):
            if "key" in inventory:
                print("You manage to open the door and get out")
            break

    while True:
        part8 = input("As you leave the room you see a figure run up the stairs do you want to shoot or chase after it?")
        if part8.lower() in ("shoot", "shoot at figure"):
            print("You take a few shots at the figure but unfortunately you miss and it's escapes up the stairs")
        elif part8.lower() in ("chase", "chase after figure"):
            print("You chase after the figure and follow it into a large room.")
            break
#This is a boss fight which the player will have to use items they have to fight the monster.
    while rep > 0:
        part9 = input("You are faced with a monsterous creature similar in look to the previous encounter, however this"
              " one is more than twice the size as the last, you need to fight and kill thew creature here and now")
        if part9.lower() in ("use handgun", "shoot", "shoot creature"):
            print("You shoot at the creature and hear it wail in pain")
            bossHealth -= 5
            rep -= 1
        elif part9.lower() in ("use knife", "attack with knife" "knife"):
            if "knife" in inventory:
                print("You slash at the creature with the knife you found and the creature falls back")
                bossHealth -= 8
                rep -= 1
        if bossHealth >= 0:
            print("You managed to kill the creature which was taking the lives of innocent people, however it seems"
                  " like there are more of them out there...")
            break

        else:
            if rep == 0:
                    print("You took too long to kill the creature and it stabbed you through the chest, killing"
                          " you instantly")
                    dead = True






























