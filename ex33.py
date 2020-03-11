i = 0
numbers = []

def while_loop(i):
    while i < 6:
        print ("At the top i is %d" % i)
        numbers.append(i)

        i = i + 1
        print ("Numbers now: ", numbers)
        print ("Att the bottom i is %d" % i)


print ("The numbers: ")

for num in numbers:
    print (num)

#  look at em 👊🏽
# while_loop(i)