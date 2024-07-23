height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇

# So the first step is to do what we did before, which is to calculate the BMI using the formula of weight divided by height squared.
bmi = weight / (height * height)


# And once we've gotten hold of that value, then we can use our if and else statements to figure out which interpretation we should give them.
# In the case where their BMI is less than 18.5, then we should print out, "Your BMI is..." whatever it is,
# and then "you are underweight." And this condition is checked in the first if statement on line 13.

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")

# Now, because there are many conditions, not just a single one, we're going to need to use the "elif statement".
# So we write elif, which stands for else if, and we can provide another condition to check. 
# Well, if the BMI is not less than 18.5, we go on to line 22. elif is the BMI less than 25.
# So that means if the first statement on line 13 was false, then line 22 actually checks to see if the BMI is between 18.5 and 25.
# And when the BMI is within that range, then the print statement, "Your BMI is X, you have a normal weight." will be printed out.

elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")

# Next, we have two further elif statements to check if their BMI is between 25 and 30 and also between 30 and 35, and we print out the corresponding interpretation.

elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")

#Finally, we cap off our conditional statement with an else which covers all the other situations.
# And in this case, because we've been pretty granular with our different conditions, the only other condition that's going to trigger the else statement is if the BMI is 35 or over.
# And in this case, we give them the final interpretation inside this print statement.
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")







# height = float(input())  # in meters e.g., 1.55
# weight = int(input())  # in kilograms e.g., 72

# bmi = weight / (height * height)

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")