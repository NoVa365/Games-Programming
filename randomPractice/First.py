#print("    /|")
#print("   / |")
#print("  /  |")
#print(" /___|")

# VARIABLES.
# Basic variables.
name = "John"
age = "35"

# Editing a string to add a variable to it.
print("There once was a man named " + name)
print(name + " Didn't like being " + age)

age1 = 78
print(age1)

print("365 Brentwood Road,\nRomford, Essex,\nGidea Park")

# WORKING WITH STRINGS.
# Using a variable and messing with the string for different outcomes.
phrase = "What's up lewis"

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

# Len gives you the length of the string.
print(len(phrase))

# This allows you to pull a specific letter or number in a string depending on where it is.
print(phrase[8])

# This allows you to check what number the letter or number is in the string.
print(phrase.index("l"))
# Can also be used for multiple letters to show you where its starts from that letter.
print(phrase.index("lew"))
# This allows you to replace strings with other words in the variable.
print(phrase.replace("What's up", "Hey"))

# WORKING WITH NUMBERS.
print(3 * (7 + 5))
print(10 % 3)

# Number variables.
my_num = 5
print(my_num)
# The str (string command) must be used to have numbers along side strings.
print(str(my_num) + " Is my favorite number")

# The abs command (absolute number).
my_num1 = -5
print(abs(my_num1))

# Gives 2 pieces of info, being a number the second being the power of the number.
print(pow(4, 6))

# Max function tells you which number is bigger. Min is smallest and round will round the number.
print(max(4, 6))
print(min(4, 6))
print(round(3.7))

# Importing python math. Allows access to some other functions.
from math import*

# Grabs the lower number and rounds down. (only works for decimals?)
print(floor(3.7))
print(floor(678))
# ceil command rounds the number up despite the decimal point.
print(ceil(3.7))

# GETTING INPUTS FROM USERS
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("hello " + name + "! You are " + age + " years old")


#print("You find a sword and a staff in a chest")
#user_pick = input("Which one do you wish to take?")
#print ("You feel the power of the weapon as you pick it up")

# LISTS
# How to display your list.
Inventory = ["sword", "axe", "staff", "tome", "bow"]
print(Inventory)
# How to pull a certain value from a list
print(Inventory[0])
# How to pull everything after a certain point in list.
print(Inventory[1:])
# Pulls inventory from a value to another value.
print(Inventory[2:4])
# How to change things in a list.
Inventory[1] = "axe"
print(Inventory[1])

# LIST FUNCTIONS
Skills = ["str", "att", "mag", "dex"]
inventory = ["sword", "axe", "magic tome", "Staff"]
print(inventory)
print(Skills)
# Adding two lists together.
#inventory.extend(Skills)
#print(inventory)

# Adding new items to a list.
inventory.append("crossbow")
print(inventory)
# Adding an item into a certain place on a list.
inventory.insert(1, "Crossbow")
print(inventory)
# Removing items from lists.
inventory.remove("Crossbow")
print(inventory)
# How to reset a list
#inventory.clear()

# Tells you what number the item is in the list.
print(inventory.index("sword"))

# Sorting a list into alphabetical order.
inventory.sort()
print(inventory)













































