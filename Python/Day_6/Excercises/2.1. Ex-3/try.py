# The first thing we know is we can get hold of a year as an integer into our program on line four and we can work with it
# through using various conditional statements to check whether if that year matches our criteria.

year = int(input())

# The first thing we're going to check is whether if that year can be divided by four with no remainder,
# and remember in order to figure out what the remainder is in programming we use the modulo symbol (%).
# So we've seen this before when we did the odd and even exercise, and in this case, it's again the same thing we can write.
# if year % 4 == 0: then that means it's cleanly divisible by four. So that means that we can proceed to the next thing to check.
# And if this is not true, so below we've got an else statement that matches this if condition, then in that case it's obviously not a leap year.
# We've already eliminated that year because it can't be divisible by four. 

# The next step is to drill it down even further. So if that year is cleanly divisible by 4, well then is it cleanly divisible by 100?
# Because according to our logic, if it's divisible by four but also divisible cleanly by 100 then it's actually not a leap year.
# This is the part that gets a little bit confusing for most people because in this case, when it's divisible by 4 and divisible by 100,
# then it is actually not a leap year and we have to continue checking the final condition.
# So that's why we've got this embedded if and else statement. So at this point we've already verified the year is cleanly divisible by four
# and we're now checking if it is cleanly divisible by 100 then we're going to continue checking.
# But if it is not divisible by 100 with no remainder and it's divisible by 4 , then it is now confirmed as a leap year,
# and this will become more obvious if you actually look at the flow chart that I provided in README.md file.
# This is just one of those peculiarities about working out which year is a leap year.
# The final check we have to do is in the case when a year is cleanly divisible by 4 also cleanly divisible by 100.
# Now the final thing is to check, well is that year also cleanly divisible by 400? Because in that case it flips again
# and it is now a leap year if all three of those conditions are met. There's many routes to navigate through the flow chart,
# but in the final section here if all three criteria is true, divisible cleanly by 4, 100 and 400, then it is a leap year,
# otherwise, if that last condition fails then it is not a leap year.
# That's why we've got three nested if and else statements in order to complete this logic in the flow chart or in the text version of how to work out a leap year.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 ==0:
      print("Leap Year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")