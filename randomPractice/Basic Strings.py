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