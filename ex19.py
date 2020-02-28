# def cheese and crackers takes the values from the arguments being passed in at line 10
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket. \n")


print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# cheese and crackers takes the variables amount of cheese and amount of crackers and passes them in as arguments
# The function is called with those variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# function run with integers and math
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# cheese and crackers runs with a mix of variables containing numerical values and integers.
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
