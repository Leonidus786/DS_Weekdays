# Now in the last lesson, we saw how we could use if, elif, else to check for multiple conditions.
# But in this case we're only checking one condition even though we have multiple, because if this first condition is true, then we would do whatever it is we need to do and then we would bypass everything else.

# if condition1:
    do A
# elif condition2:
    do B
# else:
    do C

# Now what if you were in a situation where you need to check for multiple conditions even if the previous one was already true?
# Coming back to our rollercoaster ticketing problem, if you're going on a good rollercoaster ride,
# you'd probably want to keep a picture for the memories, right? And our rollercoaster is no exception.
# We want to be able to charge users an extra $3 if they want to purchase a ticket that includes a photo. Now, this is quite interesting because this is completely independent of their age or their height.
# Even if we've already gotten their age and height and determined their ticket price, this is an extra question. Do you want a photo or not? Yes or no. If you do, then we're going to add $3 to your existing ticket price.


# To do this, we would write multiple if conditions.

# Multiple if 

# if condition1:
    do A
# if condition2:
    do B
# if condition3:
    do C

# If condition 1 is true, then do a, but then the code is going to go to the next case and check if condition 2 is also true, in which case it will do B and if the final condition is also true, it's going to do C. Whereas on the example on the above(if/elif/else) here, only one of these things, A, B, or C will be carried out.
# Comparing the example on the above where we're using if, elif, else, only one of these things A,
# B or C will be carried out. But in the multiple ifs, all three conditions are checked and if it's so happens that all three conditions are true, then A, B and C will all be executed.
# Currently, our code operates like this. --> Flowchart --> https://shorturl.at/hnINS 
# We check for their height. If they're over 120 centimeters, we check their age and depending on their age, we give them a different price ticket. What we now want is even after we've checked for their ticket price, we want to ask them a question, do you want photos with your ticket?
# And if the answer is yes, then we're going to add $3 to that bill, no matter which type of ticket they've got. And finally we give them the total bill. If they say no, then we jump straight to the total bill and just tell them the price of their ticket. So how do we implement this in our code?