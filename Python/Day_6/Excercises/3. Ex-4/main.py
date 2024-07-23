print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇

# Alright, so the first thing we're going to do is we're going to create a variable called "bill" to keep track of the ongoing price of their pizza.
# We can start that bill at $0 and then we can proceed.
bill = 0


# The next part of our code checks for the first condition, which is whether if their first input was S, M, or L,
# and we can use an if, elif, else, or we can use three if statements. You can do it in many ways, but essentially we're checking to see
# if they put an input of S, then we're going to add $15 to the bill. If they put an input of M on the first line,
# then we're going to add 20. And if the last condition, or we want to check if it was L, then we can add $25.

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25


# Now the next condition is whether if they wanted pepperoni on their pizza, and if the answer is yes,
# then we have to check against the size that they ordered. If the size was medium or large, we're going to add $3 to their bill,
# and if it was small, then we're going to add only $2. 
# So you could have used a combination. So you could have said if size == "M"  and size == "L", but in this case, what I've done is simply checked
# for just the single statement, which is unique. If the size is small, then add two. In all other conditions, add three.


if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3


# Final condition is probably the easiest. We simply want to check is the last input is "Yes" in this case, we just add $1 to the bill.
# And all of these things added up will eventually create the final price for the pizza.


if extra_cheese == "Y":
  bill += 1

# And we can print out that final price using an f-string by inserting the bill into the print statement,
# and make sure that you've got all your punctuation, your full stops, everything matching exactly what it says
# in the pdf.

print(f"Your final bill is: ${bill}.")