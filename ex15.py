# imports the module
from sys import argv

# the script, and the text file are used as modules
script, filename = argv

# Assuming "open" opens the file being passed into it for use in the rest of the script.
txt = open(filename)

# # Serves up the filename based on what is entered into the terminal.
# print ("Here's your file %r:" % filename)

# # Prints the variable "txt". ".read()", I assume, is a Python native function that reads the content of the file being opened by txt.
# print (txt.read())

# just a string being printed
print ("Type the filename again:")

# input prompt with "> " as the...prompt indicator?
file_again = raw_input("> ")

# variable that holds the basic function "open"
txt_again = open(file_again)

# reads the file being input during the raw_input prompt.
print (txt_again.read())