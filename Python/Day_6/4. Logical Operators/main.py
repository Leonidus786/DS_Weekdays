# So if we take a look just inside the console,
# and in fact, I'm going to clear the console, and I write some code here.
# Let's say that, A = 12 right? Now let's say that I wanted to check whether if is A greater than 15? Well that is going to be false.
# Now what about is A greater than 10? Well, that's going to be true.
# Now if I combined this using an and statement, I could say, well is A greater than 10 and A is less than 13 and hit enter, then I would get
# true because both A is greater than 10 and A is less than 13 are true.
# So in this case, when both conditions are true, then this entire line(a > 10 and a < 13) gets evaluated to true.
# But see what happens when just one of them is false.
# So is A greater than 15 and A less than 13? A is greater than 15 is false, A is less than 13 is true and now we get false.
# So that's what happens when you combine different conditions using and. 
# Now if you only needed one of the conditions to be true, then you could use the or operator instead.
# So if a C or D were true or if they're both true, then it'll evaluate to true. It's only when both C and D are false
# does this statement actually become false.
# Now the final one is the not operator and all that this does is it basically reverses a condition. So if the condition is false,
# then it becomes true. If it's true, then it becomes false.
# If I wrote not and then I wrote the condition A is greater than 15. A greater than 15 is definitely false, 12 is less than 15. 
# But by putting the not there it's going to reverse this, so going from false to true.

# Coming back to our rollercoaster ticketing, let's say that the rollercoaster company decided that for everybody who was
# having a midlife crisis, they would give them free tickets.
# And according to Wikipedia,(https://en.wikipedia.org/wiki/Midlife_crisis) midlife crises typically occur when you're a 45 to 55 years old.
# Let's see if we can incorporate this into our code.
# So let's say that in addition to these existing price categories, what if you had to add a separate price category for those people who are aged
# between 45 and 55 and those people get to ride for free?
# Do you think you would be able to change the code using what you've learned about logical operators in order to incorporate this addition to our program?

# Flow chart --> https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Day%203%20Logical%20Operators.drawio#R7VtZc9o6FP41zH2iY0teH0uWZpqkQy%2BZ29CXOwYrthNjUVkQyK%2BvjGWwLbEFL6HTzCSxjyVhfec7myQ68GKy%2BEKcqX%2BPXRR2gOIuOvCyA4CqAYP9SyTLVGJqXOCRwOWNNoJB8Ia4UOHSWeCiuNCQYhzSYFoUjnEUoTEtyBxC8Gux2RMOi586dTwkCAZjJxSlPwKX%2BqnUAuZGfoMCz88%2BWTXs9MnEyRrzmcS%2B4%2BLXnAhedeAFwZimV5PFBQoT8DJc0n7XW56uX4ygiB7SoR9ZTw%2FfyQD19fm%2Fc3dxF%2FzCXT6NmC6zCSOXzZ%2FfYkJ97OHICa820h7Bs8hFyagKu9u0ucN4yoQqEz4jSpdcmc6MYiby6STkT9kLk%2BVj0v%2BTAUEmGDJBV%2FmkmHomuVzwz0jvlvm7PiLBBFFEuFBEgwMU4xkZox0QZKxyiIfojnZ62i7BJ%2FcBHOsvCLO3IUvWgKDQocG8yB%2BH09Bbt%2BNdPxPiLHMNpjiIaJwbuZ8IWANuUZABthqR25Oq63mts4t0xOwu92ob0YoZR7DEbpklmqrlWaJ8TIJotRBEYICqFQlgK8UR0vfknTbMOJZohtE8zzgWcyeccXS4b01cm%2BFMGHF6Hl0pU1GZz5904LVATeLjyWjGZtl79QOKBlNnpd1XFp%2BKBNvKiDkiFC126jB7qppFlLKw9bqJFarBZX4uTpSVlld7DuPjIYRtmOr7bQscaFtq1bZ1EshA4OmAzYCKVFwDq%2B6n41MQhhc4xGTVF7o6stzE7cWU4BeUe2KBEWTWWQ2BYZHAQMJfIOGvVhd%2FNQHaCyf6J%2FEALD1EpyFcAV5QKcIlsXfLrAeuy682%2BL%2F%2FzaXPLvk%2BvOl71zdexsRzMXddNHfptD6WuesyTn4URgKzZMENUlLuqhUBrm9YgInNjhaxcMLAi9j1mGGRZG29BIOAVWKf%2BYNJ4LopgVEcvDmj1VAJhXkqw8bVex39MhmLcTZO6VsRzFYp0ENbQBlK%2FCSoDWUxVxqi%2BOxhBpa2F2etJpylnkiMR2143FwttK6OD6mEDvLUuzzwXk9tVO2p5dUIUJKZ55kBgV4cZEvd847aRA6I8lfx%2BXZWWyFa%2FtZ%2FzbLQzm4tgVKGP3%2B8PfT6PwfImj8%2BPAS9STtZKloE9DF3Pdzoid1tNJPcFFaO2laoFMLWMuJdb52LiskyepsrMcASAoQiSYQlqYNeW23Wsk9qhsD1JADHrlaqsKh8zSpthpTzCRvual9c3tzbWy8XUzXnIoYkKWUq1HTRBBuuRu3i%2Bgi0RBu0a1pOkiJlCkjdoThOHK6%2FKuElecO5lUxqGfMD%2FV5tJRNoJVN%2BvwerPJPdsnMHyhFKL6ugZrdhbXEb4iZw84tYejl6t%2B051vRpJ3qrzUTvyuuEd0VvXTkuekPNOiF6l3s3Hb3tLWYoiUVN26FmfLD4LVnmVEFXtc4%2BakNV8Hi6iLXeZNxWoYg1A1rBJPnDpnb%2BoB%2BQKpmNpkqyTH6rD1D2%2BwBhs9gYW2j0VNpejnCUqMB1Yn%2FtXCqAVzeL8AKJ91Bl%2BK6PSJwCsH3%2F%2BGI8erfgFvwKlvfPN8v%2BfVekdBtR%2FaD4vGvZJ7885M%2FnXfx0iYKv9n%2Bz5a06uDNesnnWncPqalHDh2awRx8%2BsuSZcmWnj3ZgLcRlsZxpOiwbWnthWQqVaFafPYYHUJIlCKXLfnVxLeLcooVuvm9BsYpoITXyViqSg3zXLp%2B013dVfrD2JJBbCRDZXkW2IXHkXgWofrPiJI2aH0qjorN6dSJ%2BpjRMPNKIZbbG6lzp1MfMi5x0qlTIwJTVjzwDq8BLlQ%2FqrkNyPulSbNFNWXW5Ka1VC1pbzTD3pIXdvl2u7swMSDz%2FliZG4lnjoxKjpi0FlnZtDNlhbaWmNEoKrFj9%2FQlnuMo4r9fXGjjDtcuacjA%2F%2BCgxQ0ydpPMoSMeIVzFBW5wXrVmeWoDblKSpKrCz1aZGiC3uNPwBR0ABLEVaCa8rOgPKbjdfDEzr283XK%2BHVbw%3D%3D#%7B%22pageId%22%3A%22hBWSzeyfJMC0TEZSpMNW%22%7D

# So we've currently got three conditions: age, less than 12, age between 12 and 18, and finally everybody else.
# Now instead of just finishing up there, let's go ahead and add another elif.
# And here we're going to combine two conditions. We're going to say if the age is greater than or equal to 45 and the age is less
# than or equal to 55, then we get to catch that midlife crisis window.
# Well, in this case, we're going to print something like-- we're going to say "Everything's going to be ok. Have a free ride on us!"
# And in fact, we don't need to modify the bill in any way because we know that with if, elif and else statements is that once this condition matches,
# then everything that's inside this block, so everything that's indented inside this elif is going to be carried out
# namely printing this out, and then it's going to skip the rest of this if/else block and continue on.
# Now, if they want to photo this, they'll have to pay $3 but at least their ticket is free.
# And we've been able to do this because we know about the and logical operator.
# In the next lesson, we're going to practice using logical operators and more by completing another code challenge. So for all of that and more, I'll see you there.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")