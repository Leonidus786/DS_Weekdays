# In the last challenge where we calculated the BMI, you saw how when we had a number that had a long list of numbers after the decimal point. 
# For example, if I had divided 8 by 3 and I print this out, you'll see that the value is 2.666666 and if we had just turned this 8 divided by 3 into an integer, right now it's a floating point number,
# but if I convert it into an integer, you'll see that all it does is it just chops off everything after the decimal point. 
# Instead of what we would traditionally do, which is to round the number.
# So if it's 2.5 it would go to 3, if it's 2.4 it would go down to 2.
# Now in Python it's super easy to round numbers.
# All you have to do is to use the round function like this. 
# If we write round(8 / 3) then it's going to round it into a whole number and you'll see that instead of 2 we actually get 3 now
# because 2.6 recurring becomes 3. Now if you wanted to, you can actually go a step further.
# You can specify the number of digits of precision you want to round it to.
# So if I said I want to round it to two decimal places, then I could write (8 / 3, 2) and then the number of places that I want around it to.
# So now our 2.666 recurring becomes 2.67 because I said we should round it to 2 decimal places. So if it makes it easier,
# it might be easier if I write it like this. 
# So 2.666666666 and I'm going to round it to two decimal places and again, I get the same result, 2.67. 
# Now another way of modifying numbers is instead of dividing, say 8 / 3, we can also use the floor division, so where you have two forward lashes instead of just one.
# Now we know that whenever we divide any number by any other number, the result always gets turned into a floating point number.
# Now if you didn't want that and you just wanted an integer, so a whole number chopping off all the numbers after the decimal in place,
# you can just use the floor division like this.
# And in this case, you would get 2 straight away without having to convert it into an integer.
# And in fact, if I go ahead and check the data type of the result of this calculation, you'll see that it's actually an integer
# whereas if I had just used the single, um, forward slash division, then I get a floating point number with decimal places.
# Even if this is a clean division, say 4 / 2, this is still going to become a floating point number and the number is going to be represented like this, 2.0, like so.
# Now if we had saved the results of this calculation into a variable instead, then one of the things that you can actually do is to continue performing
# calculations on this variable. So for example, I could do 4 / 2, which is going to be equal to 2. But then if I want to divide it by the 2 again,
# I could actually say result /= 2. And when I now print results, I'll actually get 1 because it's 4 / 2 then divided by 2 again.
# Now very often when you're writing code, say for example if you're keeping track of the user's score,
# so you could have score = 0 to begin with and every single time in your code say a user scores a point,
# then you can get hold of this score variable again and instead of saying score now equals the previous value of score plus one,
# you can simply use this shorthand, +=, so +=1. And now when we print score, you'll see that it's actually equal to 1.
# So instead of using +=, you can use -=, which just takes the previous version of score and removes 1 from it.
#  *= and /=.So this is really handy when you have to manipulate a value based on its previous value, which you'll have to do a lot in programming.

# print(8/3)


# print(int(8/3))
# print(round(8/3))
# print(round(8/3,2))
# print(round(2.6666666,2))
# print(8//3)
# print(type(8//3))
# print(type(8/3))

# result = 4 / 2
# result /= 2
# print(result)

# score = 0

# score = score + 1
# score += 1
# score -= 1

# print(score)


# Now the final thing I want to show you is something called F strings and this
# makes it really easy to mix strings and different data types.
# So far, up to this point,if we wanted to print, something like your score is,
# and then we wanted to print the score we have to write plus, but of course because these are different data types,
# this is a string and this is an integer, we got a type error.

# print("Your score is " + score)

# So we've had to convert this into a string before it will actually successfully
# print when both the datatypes match.

# print("Your score is " + str(score))

# Now this is quite painful and understandably a lot of programmers will need some
# slightly more convenient way of incorporating things that have different data types.
# Let's say um, the score is equal to zero.
# let's say the height is equal to 1.8 and isWinning is equal to true.
# So here we've got a integer, a float, and a boolean, and we want to mix it all into a sentence that is a string and get it printed out.
# So instead of having to convert all of these and use a whole bunch of plus
# signs and then you have to convert everything into a string, it's really, really painful, right?
# So what we can do instead is use something in Python known as an F string.


score = 0
height = 1.8
isWinning = True


# print("Your score is " + str(score))
#  f-string

# And when an F string allows us to do is in front of a string like this one,
# we type the character 'f' and it's really important that it goes in front of the
# double quotes or a single quotes if you want to write your strings like this.
# But I like to use double quotes and a lot of other Python programmers do too.
# So essentially you're adding just the character f in front of the string,
# and now this is an F string and you can start adding various values into this string.
# So for example, if I wanted to write, your score is equal to this variable score,
# then I can put that variable inside a set of curly braces like this.
# And now when I print my string, this one right here, you'll see that it says your score is zero and it does all of the converting and
# all of the stuff behind the scenes and you don't have to worry about any of this.
# So if I want to continue along, I could say your score is this, your height is adding the height and then you are winning is then let's add
# that final boolean value and get it to run.
# You can see that our entire string now prints out your score is 0, your height is 1.8 you are winning is True.
# So all of these different data types got combined into a string by using an F in
# front of the string and then using these curly braces to place our variables into this string.
# By using f strings, you cut down on a lot of the manual labor of inserting different data types into a string.
# 


print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")