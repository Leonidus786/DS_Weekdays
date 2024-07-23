
marks = 85
print(type(marks))


# This line would raise error - TypeError: can only concatenate str (not "int") to str

# print("You have got"+marks+"marks")

marks_as_str = str(marks)

print("You have got "+marks_as_str+" marks")

