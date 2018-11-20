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