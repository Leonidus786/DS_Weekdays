#Strings, Integers, Floats and Booleans

# Strings - This is just a set of characters.

# "Hello" #This word Hello is comprised of these five characters strung together.

# And we always know that strings, when we create them, We have to create them with double/single quotes around.

# Now because this is a string of characters, we can actually pull out each character individually.
# So we could , for example instead of just writing hello, we can add some square brackets.
# And inside the square brackets, we can put the index or the position of the character that we want.

# For example if I wanted to have the first character out of this word hello, I would put zero right here.

print("Hello"[0])

# It's really important to remember that programmers always start counting from zero.
# because we work with binary -- zeroes and ones.

# This method of pulling out a particular element from a string is called subscripting.
# And the numbers in between the square brackets determines which character you are going to pull out.
# So by using these square brackets and putting a number inside, we're able to dissect
# our string and pull out individual characters as and when we need it.

print("123" + "345")
# this just concatenated these two strings.

# As long as these numbers are kept inside these double quotes, then this is 
# not treated as a number by the computer.

# Integer -- this is programming lingo for just whole numbers, numbers without any decimal places.
print(123+345)

# just as we have some useful things we can do with strings.
# There's some really handy things we can do with integers.
# Commonly when we write large numbers, at least in the UK or in the US, we'd like
# to put commas in between the thousands.
# ex. 342,654,896

# In python we can replace these commas simply with underscore and it will be
# interpreted by the computer as if you had written this.
# So the computer actually removes those underscores and ignores it.
# The benefit is just for us humans to be able to visualize it more easily.

print(342_654_896)

# So I mentioned that all whole numbers no matter if they're positive or negative,
# are called integers in programming.

# So what do you call it when you actually have decimal places?
# well, they are called a float and this is short for a floating-point number.
# So, for example, if you had, the numbers of PI, you have 3.14159 and this,
# because it has a decimal place, is now a float data type.

print(3.14159)

# So if you think of the decimal point as being able to float around the number
# because it could occur at any point, then you've got yourself a floating point number.

# Boolean 

# Now the final data type is something called a boolean.
# and this is very simple. It only has two possible values, True or False.

print(True)
print(False)

# Now note how these values begin with a capital T or capital F and they don't have
# any quotation marks around them or anything.
# So this is actaully a data type which is going to be used a lot in your programs
# to test if something is true, if something is false and for your program to respond accordingly.
 