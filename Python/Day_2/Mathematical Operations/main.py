# In the previous lession we saw how we could use the plus(+) sign either to 
# concatenate strings together or as a mathematical operation where we add two
# integers or two floats, basically two numbers together.
# In this lesson I want to show you some of the other mathematical operators 
# that you have access to in addition to adding. The next obvious one is subtraction.
# So, 7 -3, you would just use the minus sign, but then when you get to multiplication
# it's little bit weird. Instead of using x or some sort of symbol, you actually
# use the asterisk. 
# Now the final one is divison and that's done using the forwardslash.



# print(7+3)
# print(7-3)
# print(7*3)
# print(6/9)


# Now one thing to notice here is that whenever you're dividing things,
# you actually always end up with a floating point number.

# print(7/6)
# print(4/2)

# And this is something that happens with divison in python.
# But at the end of the day you get the result that you need and it doesn't 
# really matter whether it it's a float or if it's a integer.

# Now the last one that's really useful is two asterisk signs and this gives you 
# access to the exponents or when you want to raise the number to a power.

# So for example, if you wanted to get a hold of 2 to the power of 2, then you would write it
# like this and 2 to the power of 2 is of course basically just 2 times 2 which is going to be equal to 4.

# print(2**5)

# Having the exponent being built into the language is one of the reasons why 
# Python is really loved by a lot of data scientists and mathematicians because 
# it's really optimized towards manipulating and handling numbers.
# Now, one of the things that you have to be careful about when you are doing these
# mathematical operations is when you have more than one operation on the same
# line of code, then there's a certain level of priority.
# So some of these operations like division or multiplication are going to be first class,
# whereas other ones are going to be more economy like the plus and minus.
# And the rule that you might've remember from high school is something called PEMDAS.

# It basically states the order of priority is parentheses, exponents, multiplication, division, addition and subtraction.

# So the things that happen first are the things inside brackets, then it's our exponents, then it's our multiplication and division.
# And finally, the lowest priority is our addition and subtraction.
# Now it's a little bit deceiving because of this order.
# It makes it seem like as if multiplication happens before division, but actually they are equally important.
# And when it actually comes to your calculations, the calculation that's most to the left is the one that will be prioritized between multiplication and division.


# So let me give you a real-life example to make this more clear.
# print(c)

# If I was to execute this entire line of code and print it out into the console, here's the time where you play computer again and guess using what you've learned here, 
#  what exactly will be printed because you will get a number printed,
# it will calculate this entire line of code for you. But the order matters.

# Now if math is not your strong point, don't worry, it's not mine either and you're the sort of person who would prefer to see it visualize.
# Then I recommend again putting this line of code in Thonny, and then go ahead and clicking on the debugging symbol and then just step into,

# So now here's another challenge for you.
# How can you change this code so that instead of getting 7, we get 3?
# How can you change this line of code given what you know about PEMDASLR?
# Alright, so this will involve a little bit of trial and error.
# And the most important tool we have access to is the parentheses or the brackets. 
# This means that we can actually isolate bits of our code, which normally have very low priority and turn them into higher priority operations.
# So in this case, we know that 3 * 3 is going to happen first, and then the multiplication, and then the addition on the left, and then the subtraction.
# But if we added a set of parentheses around our 3 + 3, then out of all of these calculations, this particular one suddenly becomes the highest priority and it will happen first.
# So if I change what I've got in Thonny to our new version and go ahead and debug through it,
# the very first calculation it's going to perform is this 3 + 3 inside the brackets and we end up with 6.
# So then it's going to go again from left to right, prioritizing multiplication and division.
# So then it's 3 * 6 is 18. 18 / 3 is 6. 6 - 3 is 3..
# Just by isolating certain calculations, you can elevate it to right at the top of the priority list and you will be able to perform the calculation that you need.
# https://thonny.org/


# print(3 * (3 + 3) / 3 - 3)