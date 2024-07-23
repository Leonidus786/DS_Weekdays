# Firstly, we know we get hold of the name1 and name2 in our variables name1, name2 on lines five and six.


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# And what we're going to do on line twelve is to combine these two names together so that we have just a single string to check.
# We write combine names equals name1 plus name2.
combined_names = name1 + name2

# The next step is to take all of the characters and make sure their casing is the same as what we're going to check it against
# because the user might have typed in capitalized names, they might have put the names in all caps, they could have put it all in lowercase,
# we don't want all of that ambiguity. So we're going to check the names against lowercase letters. 
# So we're also going to use the ".lower() method" to make our combined names into lowercase.
# That means we take our name1, name2, for example in the Input, we've got David Beckham, and Victoria Beckham.
# By combining it on line five, we now have a single variable called davidbeckhamvictoriabeckham and by making it lowercase,
# all of those letters are now lowercase letters.
lower_names = combined_names.lower()

# The next step is to calculate the first digit in the love score, which according to the rules is to check how many times
# the letter T-R-U-E occurs in both the names. So we're going to check it against our lower names,
# the combined lowercase names, and we're checking it against lowercase letters as well, t-r-u-e. 
# And then, we use the "count() method" to see how many times that letter occurs in our combined name.
# And we add those numbers all up together in order to get hold of our first_digit for our love calculator.
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# And similarly, we do the same thing for the second_digit. We count how many times the letters l-o-v-e occurs
# in the combined lowercase names, and we add all of those occurrences up to get our second_digit.
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Once we've got both digits, then we can combine them together. The way that this calculator works is we take
# the first_digit and the second_digit and we create a two-digit number.
# So we can't just add it together like maths. It's not like 9 + 8 equals 17, it's actually 9 + 8 equals 98.
# So that means, we're going to have to turn our digits, which are numbers into strings so that we combine them rather than add them up.
# To do this, we write the str() method, we wrap it around the digit that we want to turn into a string
# and then we use the plus sign (+) in order to concatenate it together so that they occur one after the other as if it was text.
score = int(str(first_digit) + str(second_digit))

# Now, the final step is to check the score against the conditions that we set out in the task_1.pdf, so we can give people an interpretation
# of their score. Because in this case, we're going to have to compare numbers against numbers, then it makes sense to turn our combined love score
# into an integer, so we wrap that combined string into an int() method to turn it into a number that we can compare against other numbers.
# All that's left to do is just to write an if, elif, else statement in order to check against the three conditions.
# If the score is less than 10 or if it's greater than 90, then we print the first statement. Otherwise, if the score is greater than
# or equal to 40 and it's less than or equal to 50, so between 40 and 50, then we print the second statement.
# And if all of those are not true, then else, we just print out their score in the third statement.
# That's all there is to this exercise.
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")