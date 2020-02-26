# argv is known as a module that's imported similar to React libraries
from sys import argv

script, first, second, third = argv

# once the prints are declared, you need to run the python file in the terminal followed by the three (in this case) variables that you'd like to set
print ("the script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)