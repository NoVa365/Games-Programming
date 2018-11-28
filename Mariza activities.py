corkyDead = False
inventory = ["axe", "tome", "staff"]
chest1 = input("You find a chest do you want to open it? ")
if chest1 == "yes":
    print("You open the chest and find a sword inside and add it to you inventory.")
    inventory.append("sword")
    print(inventory)

if chest1 == "no":
    print("You decide that you are carrying too much and do not take the sword")
    sword = False

while corkyDead == False:
    print(inventory)
    battle1 = input(" Oh no you are attacked by a Corky which weapon do you wish to use? ")
    if battle1 == "sword":
        if sword == False:
            print("you don't have a sword")

        else:
            print("You killed the Corky")
            corkyDead = True

if corkyDead == True:
    print("You find a road and move along it North")














