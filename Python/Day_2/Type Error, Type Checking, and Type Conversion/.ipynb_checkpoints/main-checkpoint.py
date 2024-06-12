# previously we saw how the len function gives us a type error when we give it a number instead of a string.

# print(len(483))

# So, let's talk a liitle bit more about data types and functions.
# and the way I think about functions is kind of like some sort of fancy machine
# that you might see in a factory, right? So, in this case we've got some sort of machine
# that's going to take potatoes into chips and we don't really care how it does it,
# but it's probably going to have to peel the potatoes, wash the potatoes, cut it up, fry it,
# and then finally return it to us as an output in the form of fries.
# Now let's say that we took the same machine that normally processes potatoes and
# we decide to get a rock and we just pass this through the function,then we're getting
# an error, right? This is basically what happened above.
# the len() function doesn't like working with integers. And by forcing this through,
# We end up with an error and our code breaks and it gives us this thing, a type error.
# Now do you remember previously we had this challenge where we asked you to get the
# get an input from the user, What is your name?  And then we use the length function
# to get the number of characters of their name. And let's just save that to a variable.
# let's call it num_char and then we print your name has num_char plus number of characters.
# So in this case you would expect it to prompt the user to enter their name.
# Let's say I write Abhishek and the length of that string  would be 8.


# num_char = len(input("What is your name? "))
# print("your name has" + num_char + "characters."  )

# the above print function would also raise a type error. So it tells you that 
# you can only concatenate strings, not integers. So in this case, we were concatenating
# a string to an integer.

# So how can we prevent these type errors and how can we see the data type that we're working with?
# well, we could use a function called type, which basically will check whatever you put
# between the parentheses and give you the type of data that it is. 

# print(type(num_char))

# So adding a string to an integer doesn't make any sense, which is why you got the type error.
# Now every so often when you're writing code and you're not quite sure what the type of data
# of something might be, then you can simply just put it inside a type check function,
# right? Like so. And then you'll get an answer.
# Now in addition to type checking, we can also do type conversion or you might hear
# it called type casting where we change a piece of data from one particular data type to another.
# So it, for eg, we know that this variable num_char has the data type of integer.
# If we wanted to turn it into a string.

# We could convert it into a string by writing -->

# num_char = len(input("What is your name? "))

# new_num_char = str(num_char)

# print("your name has " + new_num_char + " characters."  )

# So in this case we have taken a integer data type, put it inside the 
# parentheses of a str function, which takes a object in between the parentheses 
# and converts it into a string, which we then store inside this new_num_char
# and we can now use it in our print statement because all the data types of all
# the pieces of data that we're adding together have the same data type, string.

# Now you're not limited to only converting numbers into strings.
# You can covert a whole bunch of different data types.
# a = 123
# print(type(a)) # This gives you a integer

# Now let's say I converted to a string by wrapping it inside the string function, then hit enter.
a = str(123)
print(type(a))

# Let me ask you two quick questions.

# 1. what will following line of code print? 

print(70 + float("100.5"))

# This will print 170.5 but what's actually happening behind the scene is we're
# converting this string 100.5 into a floating-point number nad then we're adding 70
# to 100.5 and finally we're printing the results.


# 2. What about this line
print(str(70) + str(100))

# Well, this time we get 70100.