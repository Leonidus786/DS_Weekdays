# Here's a question. Have you ever sat in your bath and wondered, why is it that no matter how forgetful I am,
# my bath never overflows like this?
# This is something I was thinking about the other day and I realized that it's not because I'm particularly diligent. 
# I forget stuff all the time. I mean, pizza, anyone? This is what my pizzas usually look like.
# But the reason why a bathtub or the sink doesn't overflow is because of this fantastic piece of engineering, the overflow.
# So this means that whenever the water reaches beyond a certain level about here, the water starts overflowing
# so the bathtub doesn't overflow and annoy your neighbors downstairs.
# In fact, we could represent this mechanism with a conditional statement.
# When the water level is say greater than 80 centimeters, then it should drain the water.
# But if the water level is not greater than 80 centimeters, it should continue filling up the tub.
# This type of conditional statement is known as an if/else statement. Depending on a particular condition,
# we would do either A or B.
# And when we want to write Python code to represent this, it looks something like this.

water = int(input("Enter the water level(80-100): "))
if water > 80:
    print("Drain the water")
else:
    print("Continue")


# if condition:
#     do this
# else:
#     do this

# There's the keyword if, and then the condition that we're testing for and then a colon and after the colon we've got an indented block of code which should be
# executed if this condition is met, if it's true. But if it's not true, then we will skip to the else block and it's just the else keyword with a colon and then this code block would execute if the condition is false.
# So we could represent that previous bathtub situation with code that looks a bit like this.

# water_level = 50
# if water_level > 80:
#     print("Drain Water")
# else:
#     print("Continue")




# Let's say our water level is at 50 centimeters and then we would test if the water level is greater than 80 centimeters. Well, if that is the case,
# then we should drain the water. But if it's not greater than 80 centimeters, in other words else, well in this case, we should just continue filling up the bathtub.
# Let's put this into practice with a real life problem.

# Now let's say that you've gotten a job at a theme park and your first job of the day is to write some code that replaces the ticket box.
# Now there's a couple of things that you'll need to think about. Firstly, in order for somebody to actually purchase a ticket to go on the rollercoaster
# ride, they will need to be over 120 centimeters. So we have to check what their height is because if they're too short,
# then we won't be able to sell them a ticket anyways. In the README.md, I've included a link to this flow chart that I've created on draw.io.
# This is a really, really useful tool for creating any sort of flow charts or diagrams and it's really easy to use. Now, if we take a look at this flow chart,
# this is basically the logic that we have to program using our, if and else statements.
# If the person who's trying to purchase a ticket is not over 120 centimeters, then they can't ride on the rollercoaster.
# But if their height is greater than 120 centimeters, then they can ride.
# So let's try it out in tickets.py 
# you'll find some starting code in there and you can go ahead.
