# In python you can return a range of characters using the slice syntax
# Specify the start index and the end index separated by a colon, to return a part of a string

# Example; get characters from position 2 to position 5(not included)

b = "Hello, World!"
print(b[2:5])

# Note:the 1st character in the string has index 0

""" Slicing from the start.
by leaving the start index, the range will start at the first character.
Example; get the characters from the start to position 5(not included)
"""
b = "Hello, World!"
print(b[:5])

""" Slicing to the end,
by leaving the end index, the range will go to the end character
Example; get characters from position 2 all the way to the end
"""
b = "Hello, World!"
print(b[2:])


""" Negative indexing, use negative indexes to start the slice from the end of the string
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])