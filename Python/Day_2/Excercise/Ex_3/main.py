age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# The first thing we need to calculate is how many years they have left.
# So we're going to take 90 and we're going to subtract it by their age.
# But again, remember that the input comes in as a string data type.
# In order to convert it into a whole number, an integer, we need to wrap the int() function around the age,
# just like what you see on line 11.

years = 90 - int(age)

# In order to get to the number of weeks that that year is representing, we can drill it down through months
# or we can directly go there through the number of weeks.
# There are 52 weeks in a year, so we can simply multiply what's stored in the number of years by 52.
# If somebody was aged 41, then 90 - 41 = 49, and then 49 multiplied by 52 is 2,548 weeks.

weeks = years * 52

# Finally, we can print out using an f-string, telling the user they have however many weeks left,
# and we're substituting the weeks variable into the f-string using the curly braces here.
# And there you have it, that's the solution.
print(f"You have {weeks} weeks left.")