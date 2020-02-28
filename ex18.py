# this one is like your scripts with argv
## I totally get this. def print_two is being passed *args which is declared as a variable holding arg1 and arg2
## It then prints arg1 and arg2
def print_two(*args):
    arg1, arg2 = args
    print ("arg2: %r, arg2: %r" % (arg1, arg2))

#ok, that *args is actually pointless, we can just do this
## def print_two_again is passed the actual arguments arg1 and arg2 outside of a containing variable.
## It then prints as it did above.
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
## Same principle as print two again but with only one argument being passed.
def print_one(arg1):
    print ("arg1: %r" % arg1)

# this one takes no arguments
## Same principle as the above functions but no argument is being passed.
## Only prints the string within the function. 👍🏽
def print_none():
    print ("I got nothin'...")

## Calling the functions
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()