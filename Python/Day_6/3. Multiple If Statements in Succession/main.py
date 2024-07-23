# This is previous code we have done during nested If.
# print("Welcome to rollercoaster!")

# height = int(input("What is your height in cm? "))



# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")




# Well, first let's change these print statements. Instead of giving them the bill at each of these steps,
# I'm going to tell them which type of ticket they're eligible for.

# So the next thing to do is to ask them whether if they want a photo or not.
# So I'm going to need to use an input, but the question is where do I put that?
# Now the correct answer is that it has to be at the same indentation level as this age if block is. So you can imagine this whole thing with the,
# if elif and else as sort of belonging together. 
# Because they all relate to one thing: what is their age and which type of ticket are they eligible for.
# Now, outside of that if statement, I'm going to create an input and ask the user, do you want a photo taken? Type Y for yes or N for no.
# And then I'm going to save their input inside a variable called wants_photo.
# So now I'm going to use an if statement to check what their answer was. If it was true, then I'm going to add $3 and if it was false,
# I'm just going to skip to giving them their ticket price.
# So here is where I write my if statement. Notice how it's at the same indentation level as this previous set of if statements.
# But it's not at the same indentation level as this set of if statement. So essentially what's happening is once I've checked their age,
# then I'm going to check whether if they want a photo or not. And this is going to apply to everybody no matter their age.
# So if wants_photo is equal to Y, well in this case I'm going to go and add $3 to their bill.
# But how can I add $3 the bill when I don't have a variable to vary?
# So instead of using these print statements, I'm going to create a variable up here called bill and I'm going to set it to equal zero.
# Now in addition to printing to the user how much their ticket is, I'm going to set the bill to the price that they're supposed to pay.
# So if age is less than 12 bill is equal to $5, if age is less than 18 then the bill is equal to $7, and finally for everybody else, he bill is equal to $12. 
# So now depending on these conditions, the variable bill is going to be changed to a different number.
# But once we land in this if statement, I'm going to have to add $3 to their bill no matter which value it is at the moment.
# So effectively, what I want to do is bill equals the current value of bill plus $3. So if bill was $7,
# then this new value bill should be $10. If bill was $12 then it should now be $15.
# Now in Python as well as many other languages, there's actually a slightly shorter way of writing this(bill = bill + 3).
# When you want to increase the current value that's held in a variable and you wanna save it back into the variable,
# you can simply write plus equals. So bill += 3 is the same as bill = bill + 3.
# Now, no matter what the value of bill is before it reached this if statement, I'm still going to add $3 to it. Now after this
# Now after this if statement is completed, I don't actually have to write a companion else statement because in this case,
# if the answer is no, then we're simply going to do nothing. We're not going to do anything to the bill. Instead,
# I'm just going to skip ahead and print to the user their final bill.
# And I'm going to use fstrings to insert the value that the bill variable has into this print statement. Now for your code to work,
# the indentation matters a huge deal because the computer will think you want it to do different things depending on the indentation.
# So notice how this indentation shows that this bill plus three is to be executed when this (wants_photo == "Y")condition is true,
# but this print(print("Your final bill is {bill}")) statement is not indented to the same level and effectively it's going to 
# happen after this (if wants_photo == "Y":) if statement has been executed. 
# So you can play around with indenting this print statements, un-indenting it and see what the difference is.
# But now I'm going to go ahead and hit Ctrl + Alt + N on Windows to run my code and I'm going to go ahead and try and get a ticket.

print("Welcome to rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.") 
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        #Add $3 to their bill
        # bill = bill + 3
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
