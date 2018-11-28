#Dead function for the the win loss state of the game.
#dead = False
#Players inventory for the game.
inventory = ["axe", "shield"]
#Opening the chest and saying yes adds the sword inside the chest to the players inventory.
chest1 = input("You find a chest would you like to open it? ")
if chest1 == "yes":
    print("You open the chest and find a sword ")
    inventory.append("sword")
    print("Your inventory is now", inventory)

# If the player chooses no they do not open the chest and do no obtain the sword.
if chest1 == "no":
    print("You decide not the open the chest, thinking it could be a trap ")

# Next part of the game if the player chooses to not open the chest.
if chest1 == "no":
    print("After leaving the chest you leave the room and walk out onto the road")

# Next part of the game if the player chooses to open the chest.
if chest1 == "yes":
    print("After leaving the chest with your brand new sword you leave the room and walk out onto the road")

# Sets up the next choice of where to go for the player.
road1 = input("You can either go East or West down the road.\nThe Eastern route has a small glimpse of a town.\nThe Western route shows a dark forest.\nWhich way do you wish to go? ")

# If the player chooses to go East then it will display this message.
if road1 == "east":
    print("You head east and fnd yourself at the town of Dunebridge or as the sign would show")

# If the player chooses West then it will display this message.
if road1 == "west":
    print("You choose to go West and find yourself at the afprmentioned forest.\nYou can feel the evil coming from the forest ")

# Sets up the player if they want to enter the forest.
forest1 = input("Would you like to enter? ")
# Player enters the forest with the next command.
if forest1 == "yes":
    print("You enter the forest and obtain a real feeling of death all around you ")
# Last chance for the player to turn around.
forest2 = input("Do you wish to turn back? ")
if forest2 == "no":
    print("You hear a noise from behind you and turn around to find a huge troll has crept up on you ")

if forest2 == "yes":
    print("You turn back out of the forest look around")

# Next line starts a decision to fight or flight with the troll.
troll1 = input("Do you wish to fight the troll? ")
if troll1 == "no":
    print("You attempt to run from the troll and hit your head on a tree branch\nThe troll catches up to you and kills you")
    dead = True
if troll1 == "yes":
    input("Which weapon do you wish to use? ", inventory)
