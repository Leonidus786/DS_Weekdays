# Which number do you want to check?
number = int(input())


# The first thing we're going to check using an if statement is if the value that's stored
# in our variable number is divisible by two and has no remainder, and we're going to do this using
# the modulo, so number % 2, and then we use the double equal (==) sign to check to see if it equals 0.
# And this is equivalent to saying if number divided by 2 has no decimal places, well then in that case
# it must be an even number. So that's why on the next line, Line 19, we have an indented print statement.
# This print statement is going to be carried out if the Line 18 condition is true.
# If the input was indeed an even number, say it was Number 4, 4/ 2, 2 goes into 4 twice, and there is no remainder.
# So therefore the modulo operator gives us a result of 0. So if that condition is true, it's going to fall
# into the indented print statement and printout, "This is an even number."



# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")



# If the input was indeed an even number, say it was Number 4, 4/ 2, 2 goes into 4 twice, and there is no remainder.
# So therefore the modulo operator gives us a result of 0. So if that condition is true, it's going to fall
# into the indented print statement and printout, "This is an even number."
# Alternatively, or in this case, in the else condition, so if Line 18 condition was false, it did not work
# and there was a remainder, then we're going to print out, "This is an odd number." This is a way that we can manipulate numbers and check them and use what we learned
# about conditionals to check if a condition is true and behave in a certain way, or if that condition was false,
# then our program should behave in a different way.