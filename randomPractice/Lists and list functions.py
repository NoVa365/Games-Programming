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
# Reversing a list.
inventory.reverse
print(inventory)
# Copying a list.
inventory.copy()
inventory2 = inventory.copy()
print(inventory2)

