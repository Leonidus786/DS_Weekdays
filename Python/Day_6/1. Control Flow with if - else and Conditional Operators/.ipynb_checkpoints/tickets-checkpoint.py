# All that I've got here is a print statement that says "Welcome to the rollercoaster" as well as 
# an input asking the user for their height in centimeters and then converting the string into a whole number, an integer, and
# then I'm storing it inside this variable called height.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


# Now we're going to check whether if the height that the user has typed in is greater than 120. So we use the keyword if and then we check if the height is
# greater than 120 and then we add the colon and now when I hit enter, you'll notice that the code editor has automatically indented me slightly over.
# I'm not over here because in Python the spacing and indentation is really, really important.
# It tells the computer that the code that I'm about to write is what should be executed when this condition is met.
# So what should happen? If your height is over 120 then we will just print You can ride the rollercoaster!.
# But what should we print if height is not greater than 120? Well, in this case, we would use the else statement to catch when that happens.
# And it's really important that you don't write the else here because this is indented over. Instead, you want it to be at the same indentation level as the if statement.
# These two are essentially a pair, if and else. Now, after the else keyword, we again add a colon and then we hit enter and we're now indented again.
# And here we can write the code that should happen if this condition is false.
# "Sorry, you have to grow taller before you can ride."

# if height > 120:
#     print("You can ride the rollercoaster!.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# So the really important things here are the condition which we're testing for, is the value of height greater than 120, the syntax of this code
# so the keywords if and else as well as the colons that come after each of these lines. And finally also the indentation.
# Everything that is indented after the if is a block of code. So this is indented and it's effectively inside this if. 
# So this line of code lives inside the else statement. This block of code lives inside the if statement. And if you mess up on the
# indentation then you're probably going to get an indentation error telling you that this line 21 probably should be indented.
# But when we do actually correct it and we hit run, let's say that our height is 130 centimeters, then we get back, you can ride the rollercoaster.
# But if our height was say 90 centimeters, then we get a different outcome. We get, sorry, you have to grow taller before you can ride. So by using,
# if and else statements we're able to get our code to do different things, either printing this line or printing this line depending on a condition that
# we're testing for. Now, when we use this greater than sign,effectively what we're saying is that is the height greater than 120 which means that it does not include 120.
# In fact, if I run this code and if I type in my height as 120 then actually goes into the else block and prints this.

# So if we wanted to include 120 centimeters so that all the people who are exactly 120 centimeters can ride the rollercoaster,
# then instead of just using a greater than symbol,  we have to write greater than or equals. So these two symbols have to be next to each other.
# And now when I run my code and I write 120, you'll see that it's now falling into this block of code and it's telling me that I can ride the roller coaster. Now,
# these are called comparison operators and we've already seen greater than, so lesser than is pretty self explanatory.




if height >= 120:
    print("You can ride the rollercoaster!.")
else:
    print("Sorry, you have to grow taller before you can ride.")



# But we've also seen greater than or equal to and lesser than or equal to.
# So if you want to include a particular number, a particular value, when you do these comparisons, you would be using these instead.
# Now in this table, there's also the equal to and not equal to.

# For example, if you wanted to check if somebody's height is equal to precisely 120 then you 
# would use two equal signs. And very often it gets a little bit confusing, especially if you're new to programming when you're typing equal signs,
# because sometimes we're typing one and other times we're typing two.
# It's important to remember that when you have one equal sign, it means that you're assigning this value to this variable.
# But when you have two equal signs, you are checking to see if the value on the left is equal to the value on the right and they're completely different.
# Now, the good thing is that when you get it wrong, usually you'll get enough clues in the error to actually hint to you,
# Hey, maybe there's something that's wrong here, right? Cause the syntax doesn't look right. For this to be a condition,
# it has to be something that evaluates to true or to false. And height =120 does not evaluate to either.
# So by changing it to this, height ==120 we're saying if height is equal to 120 then we'll execute this line of code
# or any other lines which are in the same block of code.
# But if the height is not equal to 120 then we're going to execute this block of code. So if I write 120 then that works.
# But if I write 121 then it does not work. 
# Similarly, you can also check for not equals to(height != 120), which just flips it around.
# But in our case, it makes sense to say if the height is greater than or equals 120(height >= 120) then you can ride the rollercoaster.
# But otherwise you cannot ride the rollercoaster. By using, if and else statements, we can get our computer to do different things and respond differently depending
# on different conditions.
# So in the next lesson, I've got a coding exercise for you. I'll see you there.



# if height = 120:
#     print("You can ride the rollercoaster!.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")