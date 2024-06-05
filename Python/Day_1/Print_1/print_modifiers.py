# In the first print statement we want to have some double quotes around a word hello. 
#But notice the color coding here because the computer reads from left to right when it sees the first 
#double quote it thinks this is the beginning of text and then it sees the second double quotes 
# at the beginning of word hello it thinks that is the end of the text.
# So then after the end of the text well it's code.

#This will raise a error.
# print("She said: "Hello" and then left.")

# So how to solve this --> well we have two ways to do so.

print('She said: "Hello" and then left.')

print("She said: \"Hello\" and then left.")