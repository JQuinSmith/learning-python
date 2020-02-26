# A variable with a string containing an integer value
x = "There are %d types of people." % 10

# A variable that holds a string value
binary = "binary"

# Another variable that holds a string value
do_not = "don't"

# A fourth variable that holds a string that references the values of "binary" and "do_not" with %s
y = "Those who know %s and those who %s." %  (binary, do_not)

# prints the value of x
print (x)

# prints the value of y
print (y)

# prints x "regardless"(?)
print ("I said: %r." % x)

# prints y as a string
print ("I also said: '%s." % y)

# boolean value
hilarious = False

# Another variable that returns a string "regardless"(raw). That's how I'm going to refer to it.
joke_evaluation = "Isn't that joke so funny?! %r"

# printing a string and hilarious "regardless"
print (joke_evaluation % hilarious)

# a variable that holds a string
w = "This is the left side of..."

# one final variable that holds the other half of a string
e = "a string with a right side."

# print that concatenates w and e
print (w + e)