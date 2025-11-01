# string data type in python is specified using either a single quote or double quote
# multiline string is assigned to a variable using 3 quotation marks

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# strings in python are arrays
# Square brackets can be used to access elements of the string

a = "Hello, World!"
print(a[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop
# To find the length of a string in python we use the len() function as below
b = "Hello, World!"
print(len(a)) 

# We use the keyword in to check if a certain character or phrase is present in a string and not in 
# if the phrase is not present
txt = "The best things in life are free!"
if free in txt:
    print("Yes, 'free' is present.")
    