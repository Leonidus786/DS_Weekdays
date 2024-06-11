# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Now, the first thing we want to do is to convert the numbers that we're getting through the inputs into numbers that we can work with
# and do mathematical operations on.
# So that means on line 12, you'll see that I've created the weight_as_integer variable to store the weight input as a whole number.
# So I'm converting, in this case, in the example input 69 into a number that I can multiply or add and use later on. 
weight_as_int = int(weight)

# On line 20, I'm converting the height that is coming in with height in meters. 
# And because none of us have one meter or two meter, we're usually somewhere in between the two. 
# This is usually represented as a floating point number. So there's a decimal point in there.
# For example, I am 1 meter 79, and that will be 1.79 meters.In this case, we're going convert that input into a different data type, 
# one that can store decimal places, and that is the "float data type". So we wrap the float around the height variable, and we can turn that input 1.63 in the sample input
# into a floating point number, which again can be used in our calculations later on.
height_as_float = float(height)

# We can calculate the BMI using various methods.
# One method and probably the shortest method, but this would involve a little bit of Googling around,
# is to figure out how to use the exponent operator (**) in Python.
# Now, we haven't talked about this, but it's good to get used to the idea that there are multiple ways of doing everything.
# And just because you did it differently doesn't mean it's wrong.
# So I wanted to present you with many ways.
# Now, the exponent operator is equivalent to a math where you see that super scripted number, so the little number at the top.
# In this case, we need to square the height, so that means multiplying the height by itself, 
# or in math, this is called raising the height to a power of two. And we can do that in Python using the double asterisk operator.
# So height as a float, two asterisks, and then the number two (height_as_float **2) will square the height.
# And then all we have to do is do weight divided by height squared, and we end up with our BMI.
# An alternative way of doing this is by using parentheses. You might remember from high school maths,in the US it's called PEDMAS and in the UK it's called BODMAS, but brackets always come before any other operation.
# In this case, we can't simply just write weight divided by height times height, because the first operation that's going to be calculated
# is weight divided by height,and it's going to give us erroneous answers.
# But by wrapping height times height in a set of parentheses, we ensure that part of the operation gets carried out first, and then we take the result
# and then we divide weight by the result.
# This is more likely the way that you might have solved this, but you might have had an error because you forgot about the parentheses.
# So this is something to note.
# Finally, we can convert the BMI into a whole number, so rounding it if necessary, and then we print it out as the solution.

bmi = weight/height**2
print(int(bmi))
