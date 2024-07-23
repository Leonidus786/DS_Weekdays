# print("Welcome to rollercoaster!")

# height = int(input("What is your height in cm? "))


# if height >= 120:
#     print("You can ride the rollercoaster!")
#     # So the place where we're going to nest our if statement is inside here. Notice how it's indented. So it's already inside this if block, and above statement already has to be true.
#     # Now here we're going to create another if and else statement and the condition checks for their age. So we better ask them for an age.
#     # Let's say age equals convert the inputs to an int and "what is your age?"
#     age = int(input("What is your age? "))
#     #So now that we've gotten hold of their age, we can see if their age is less than or equal to 18. Well in this case we're going to give them the $7 ticket.

#     if age <= 18:
#         print("Please pay $7.")

#     # But else namely, if this is not true, if their age is over 18, well, in that case, we're going to give them the $12 ticket.
#     # So now we have a nested if statement, because this if and else statement lives inside this if statement.
#     # So this condition will only be checked if this is already deemed to be true.

#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Now the first thing I'm going to check is if the age is

print("Welcome to rollercoaster!")

height = int(input("What is your height in cm? "))

age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    # Now the first thing I'm going to check is if the age is less than 12. Under this condition, they should pay $5. So let's change that to five.

    if age < 12:
        print("Please pay $5.")
    # Now the next condition should be created using an elif, which stands for else if. So it means, if above condition is not true else if, can you check if this is true?
    # Well in that case then we should do this. For example, if the age is not less than 12, so they're over 12, then are they under 18? 
    # Well then this condition basically catches everybody who's between 12 and 18. 
    elif age <= 18:
        print("Please pay $7.")
    # And finally, if they're not less than or equal to 18 and they're not less than 12 then that's everybody else who is over 18.

    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")