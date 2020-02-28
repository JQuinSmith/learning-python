from sys import argv

script, input_file = argv

# 'f' is a variable that represents the file being read.
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

# a variable declared that opens the file set when the script is run in the terminal
current_file = open(input_file)

print ("First let's print the whole file: \n")
# prints the contents of current_file - in this case, test.txt
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")
# I can only assume this reverts the current_file to its original state 🤷🏾
rewind(current_file)

print ("Let's print three lines:")
# Variable with a value of 1 with a function that prints that line within test.txt
current_line = 1
print_a_line(current_line, current_file)

# Variable with a rudimentary increment to hit line 2 within test.txt
current_line = current_line + 1
print_a_line(current_line, current_file)

# Same as above but for line 3 within test.txt
current_line = current_line + 1
print_a_line(current_line, current_file)