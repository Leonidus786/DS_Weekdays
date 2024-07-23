# In previous lessons, we learned about using the if and else statements to check whether if somebody is over 120 centimeters or not and allow them to actually purchase a ticket if they are over a certain height. Now in addition to the height, there's another condition that we need to check for, namely their age. 
# If somebody is over 18 years old and they should be paying the adult price, which is let's say $12. But if they are 18 or under, then they should only be paying $7. So how can we represent this extra condition that we need to check for in our code?
# Well, we could use something called a nested if/else statement. We've seen our, if/else statements look like this where it's only got two choices.

# if condition:
    do this
# else:
    do this

# If this condition is true, do this, otherwise do that.
# But in a nested if statement, once the first condition has passed, we can check for another condition. And then we can have another if/else statement inside this if condition. 

# if condition:
#    if another condition:(In order for this thing to happen, top has to be true and this also has to be true.)
        do this
#    else:(In order for this to happen, top condition has to be true but above condition has to be false.)
        do this
# else:
    do this


# So essentially the computer first looks at the larger picture, which is the first condition and decides on whether if it should go into the else block here or if it should go into the nested block inside the if statement.
# So now this is what our flow chart looks like. In the first if statement we check whether if their height is over 120 centimeters. If no, then the if statements all end. You can't ride, you can't buy a ticket.
# But if yes, we actually take them to yet another if statement where we check their age. If their age is 18 or under, then we give them a $7 ticket. If they're over 18 then they have to pay $12.


# https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1J7_rw1flGeF0hmc_zrMzPX7t6xkbcsiX%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D


# Now let's say our situation got a little bit more complex. The boss comes over, checks our code and says, wait a wait, wait, wait,
# there's actually more price tiers than that. In fact, if you're less than 12 years old, you pay $5. If you're between 12 and 18 you pay $7 and if you're over 18 then you pay the
# full adult price, which is $12. Now there are three possibilities, so how do we represent this in our if statement?

# < 12 "$5"
# 12-18 "$7"
# > 18 "$12"

# Well, we could use something called the elif. Instead of having a simple if/else statement where there's only one condition. If it's true, do this.Otherwise do that.
# You can add as many elif conditions as you want. So we can check for condition 1. If that's true, then do a, but if that's not true,
# then we can continue and check for condition 2. If condition 2 is true, well then we can do B. And finally,
# if none of those conditions were true, we can do this final thing.

# if condition1:
    do A
# elif condition2:
    do B
# else:
    do this

# Our flow chart now looks something like this and this is the logic that we're trying to program. Once we're inside this nested if statement, we're going to check if the age is under 12 in which case they should pay $5. If they're between 12 and 18 then they should pay $7 and finally if they're over 18 then they should pay $12.

# https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload#%7B%22pageId%22%3A%22bzYDor7Mf7Ch-uxfBpj_%22%7D

# Now remember that we can use as many elif conditions between the if and else as we like.So I could add another elif that checks whether if the age is less than, say, 22 well in this case, do something else. And then I can keep going with these elifs until I'm done with all my conditions.

# NExt xhallange ex-2